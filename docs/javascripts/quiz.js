// Interactive MCQs.
// Markup (see planning/STRUCTURE.md):
//   <div class="quiz" markdown>
//     <p class="quiz-q">Question</p>
//     <ul class="quiz-options"><li>Wrong</li><li data-correct>Right</li></ul>
//     <div class="quiz-explain" markdown>Why</div>
//   </div>
// Clicking an option marks it right/wrong, reveals the correct one and the explanation.

function initQuizzes() {
  document.querySelectorAll(".quiz:not([data-ready])").forEach((quiz) => {
    quiz.dataset.ready = "true";
    const options = quiz.querySelectorAll(".quiz-options > li");
    const explain = quiz.querySelector(".quiz-explain");
    if (explain) explain.hidden = true;

    const reset = document.createElement("button");
    reset.type = "button";
    reset.className = "quiz-reset";
    reset.textContent = "Try again";
    reset.hidden = true;
    quiz.appendChild(reset);

    options.forEach((option) => {
      option.tabIndex = 0;
      option.setAttribute("role", "button");
      const choose = () => {
        if (quiz.classList.contains("answered")) return;
        quiz.classList.add("answered");
        const correct = option.hasAttribute("data-correct");
        option.classList.add(correct ? "chosen-correct" : "chosen-wrong");
        options.forEach((o) => {
          if (o.hasAttribute("data-correct")) o.classList.add("is-correct");
        });
        quiz.classList.add(correct ? "got-it" : "missed-it");
        if (explain) explain.hidden = false;
        reset.hidden = false;
      };
      option.addEventListener("click", choose);
      option.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          choose();
        }
      });
    });

    reset.addEventListener("click", () => {
      quiz.classList.remove("answered", "got-it", "missed-it");
      options.forEach((o) => o.classList.remove("chosen-correct", "chosen-wrong", "is-correct"));
      if (explain) explain.hidden = true;
      reset.hidden = true;
    });
  });

  // Number the quizzes on the page so they can be referred to.
  document.querySelectorAll(".quiz-q").forEach((q, i) => {
    if (!q.dataset.num) {
      q.dataset.num = String(i + 1);
    }
  });
}

// Material's instant navigation exposes document$; fall back to DOMContentLoaded.
if (typeof document$ !== "undefined") {
  document$.subscribe(initQuizzes);
} else {
  document.addEventListener("DOMContentLoaded", initQuizzes);
}
