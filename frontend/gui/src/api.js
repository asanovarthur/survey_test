import axios from "./axios-config";

export async function fetchTests() {
  const data = await axios.get("/tests/").then(response => response.data);
  return data;
}

export async function fetchQuestionsById(testId) {
  const data = await axios
    .get("/tests/questions/")
    .then(response =>
      response.data
        .filter(question => question.test === testId)
        .sort(
          (question1, question2) =>
            question1.positionInTest - question2.positionInTest
        )
    );
  console.log(data);
  return data;
}

export async function addQuestionToTest(question) {
  const data = await axios.post("/tests/questions/create", question).then(response => response.data);
  return data;
}

export async function destroyQuestion(question) {
  const url = '/tests/questions/destroy/' + question.id;
  const data = await axios.delete(url, question).then(response => response.data);
  return data;
}

export async function addTest(test) {
  const data = await axios.post("/tests/create", test).then(response => response.data);
  return data;
}

export async function updateTestTitle(test, title) {
  test.title = title;
  const url = '/tests/update/' + test.id;
  const data = await axios.put(url, test).then(response => response.data);
  return data;
}

export async function updateQuestion(question, text, positionInTest) {
  question.text = text;
  question.positionInTest = positionInTest;
  const url = '/tests/questions/update/' + question.id;
  const data = await axios.put(url, question).then(response => response.data);
  return data;
}

export async function destroyTest(test) {
  const url = '/tests/destroy/' + test.id;
  const data = await axios.delete(url, test).then(response => response.data);
  return data;
}

export async function fetchTestResults() {
  const data = await axios.get("/tests/test_results/").then(response => response.data);
  return data;
}

export async function addTestResult(testResult) {
  const data = await axios.post("/tests/test_results/create", testResult).then(response => response.data);
  return data;
}

export async function addQuestionAnswer(questionAnswer) {
  const data = await axios.post("/tests/question_answers/create", questionAnswer).then(response => response.data);
  return data;
}
