const STORAGE_KEY = "new-math-skill-tree-progress-v1";

const elements = {
    title: document.getElementById("tree-title"),
    subtitle: document.getElementById("tree-subtitle"),
    globalProgress: document.getElementById("global-progress"),
    board: document.getElementById("board"),
    loadError: document.getElementById("load-error"),
    loadErrorText: document.getElementById("load-error-text"),
    pickJson: document.getElementById("pick-json"),
    jsonFileInput: document.getElementById("json-file-input"),
    detailChapter: document.getElementById("detail-chapter"),
    detailTitle: document.getElementById("detail-title"),
    detailSummary: document.getElementById("detail-summary"),
    detailStatus: document.getElementById("detail-status"),
    detailPrerequisite: document.getElementById("detail-prerequisite"),
    detailItems: document.getElementById("detail-items"),
    toggleComplete: document.getElementById("toggle-complete"),
    resetProgress: document.getElementById("reset-progress")
};

const state = {
    data: null,
    selectedChapterId: null,
    selectedSkillId: null,
    completedSkillIds: new Set()
};

bootstrap();

async function bootstrap() {
    bindEvents();

    try {
        state.data = await loadData();
        restoreProgress();
        initializeSelection();
        render();
    } catch (error) {
        console.error(error);
        elements.subtitle.textContent = "加载失败";
        elements.loadErrorText.textContent =
            "无法直接读取 skills.json。你可以点击下面按钮，手动选择 skill_tree 目录里的 skills.json 文件继续运行。";
        elements.loadError.classList.remove("hidden");
    }
}

function bindEvents() {
    elements.pickJson.addEventListener("click", () => {
        elements.jsonFileInput.click();
    });

    elements.jsonFileInput.addEventListener("change", async (event) => {
        const file = event.target.files?.[0];
        if (!file) {
            return;
        }

        try {
            const text = await file.text();
            state.data = JSON.parse(text);
            restoreProgress();
            initializeSelection();
            elements.loadError.classList.add("hidden");
            render();
        } catch (error) {
            console.error(error);
            elements.loadErrorText.textContent =
                "所选文件不是有效的 skills.json，请检查 JSON 格式后重试。";
            elements.loadError.classList.remove("hidden");
        }
    });

    elements.toggleComplete.addEventListener("click", () => {
        const currentSkill = getSelectedSkill();
        if (!currentSkill) {
            return;
        }

        const { chapter, skill, skillIndex } = currentSkill;
        const canComplete = isCompletable(chapter, skillIndex, skill.id);
        if (!canComplete) {
            return;
        }

        if (state.completedSkillIds.has(skill.id)) {
            state.completedSkillIds.delete(skill.id);
        } else {
            state.completedSkillIds.add(skill.id);
        }

        persistProgress();
        render();
    });

    elements.resetProgress.addEventListener("click", () => {
        state.completedSkillIds.clear();
        persistProgress();
        render();
    });
}

async function loadData() {
    const response = await fetch("./skills.json", { cache: "no-store" });
    if (!response.ok) {
        throw new Error(`Failed to load skills.json: ${response.status}`);
    }
    return response.json();
}

function restoreProgress() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) {
            return;
        }

        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed.completedSkillIds)) {
            state.completedSkillIds = new Set(parsed.completedSkillIds);
        }
    } catch (error) {
        console.warn("Failed to restore progress", error);
    }
}

function persistProgress() {
    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ completedSkillIds: Array.from(state.completedSkillIds) })
    );
}

function initializeSelection() {
    const firstChapter = state.data?.chapters?.[0];
    const firstSkill = firstChapter?.skills?.[0];
    if (!firstChapter || !firstSkill) {
        return;
    }

    state.selectedChapterId = firstChapter.id;
    state.selectedSkillId = firstSkill.id;
}

function render() {
    elements.title.textContent = state.data.title;
    elements.subtitle.textContent = state.data.subtitle;

    renderBoard();
    renderDetail();
    renderGlobalProgress();
}

function renderBoard() {
    elements.board.innerHTML = "";

    state.data.chapters.forEach((chapter) => {
        const completedCount = chapter.skills.filter((skill) => state.completedSkillIds.has(skill.id)).length;

        const column = document.createElement("section");
        column.className = "chapter-column";

        const head = document.createElement("div");
        head.className = "chapter-head";
        head.innerHTML = `
            <div>${chapter.title}</div>
            <div class="chapter-progress">${completedCount} / ${chapter.skills.length} 已点亮</div>
        `;
        column.appendChild(head);

        const list = document.createElement("ol");
        list.className = "chapter-path";

        chapter.skills.forEach((skill, skillIndex) => {
            const item = document.createElement("li");
            item.className = "skill-node";

            const button = document.createElement("button");
            button.type = "button";
            button.className = "skill-button";

            const selected =
                state.selectedChapterId === chapter.id && state.selectedSkillId === skill.id;
            const completed = state.completedSkillIds.has(skill.id);
            const locked = !completed && !isCompletable(chapter, skillIndex, skill.id);

            button.dataset.selected = String(selected);
            button.dataset.completed = String(completed);
            button.dataset.locked = String(locked);
            button.innerHTML = `
                <span class="skill-icon" aria-hidden="true">${skill.icon}</span>
                <span class="skill-name">${skill.title}</span>
                <span class="skill-tag">${completed ? "已点亮" : locked ? "需前置技能" : "可查看 / 可点亮"}</span>
            `;

            button.addEventListener("click", () => {
                state.selectedChapterId = chapter.id;
                state.selectedSkillId = skill.id;
                render();
            });

            item.appendChild(button);
            list.appendChild(item);
        });

        column.appendChild(list);
        elements.board.appendChild(column);
    });
}

function renderDetail() {
    const selected = getSelectedSkill();
    if (!selected) {
        return;
    }

    const { chapter, skill, skillIndex } = selected;
    const completed = state.completedSkillIds.has(skill.id);
    const prerequisite = skillIndex === 0 ? null : chapter.skills[skillIndex - 1];
    const completable = isCompletable(chapter, skillIndex, skill.id);

    elements.detailChapter.textContent = chapter.title;
    elements.detailTitle.textContent = skill.title;
    elements.detailSummary.textContent = skill.summary;
    elements.detailStatus.textContent = completed
        ? "已点亮"
        : completable
          ? "可点亮"
          : "未解锁";
    elements.detailPrerequisite.textContent = prerequisite ? prerequisite.title : "无";
    elements.toggleComplete.disabled = !completed && !completable;
    elements.toggleComplete.textContent = completed ? "取消点亮" : "点亮技能";

    elements.detailItems.innerHTML = "";
    skill.items.forEach((entry) => {
        const card = document.createElement("article");
        card.innerHTML = `
            <h4>${entry.title}</h4>
            <p>${entry.content}</p>
        `;
        elements.detailItems.appendChild(card);
    });
}

function renderGlobalProgress() {
    const allSkills = state.data.chapters.flatMap((chapter) => chapter.skills);
    const done = allSkills.filter((skill) => state.completedSkillIds.has(skill.id)).length;
    elements.globalProgress.textContent = `${done} / ${allSkills.length}`;
}

function getSelectedSkill() {
    for (const chapter of state.data.chapters) {
        if (chapter.id !== state.selectedChapterId) {
            continue;
        }

        const skillIndex = chapter.skills.findIndex((skill) => skill.id === state.selectedSkillId);
        if (skillIndex === -1) {
            return null;
        }

        return {
            chapter,
            skill: chapter.skills[skillIndex],
            skillIndex
        };
    }

    return null;
}

function isCompletable(chapter, skillIndex, skillId) {
    if (state.completedSkillIds.has(skillId)) {
        return true;
    }

    if (skillIndex === 0) {
        return true;
    }

    const previousSkill = chapter.skills[skillIndex - 1];
    return state.completedSkillIds.has(previousSkill.id);
}
