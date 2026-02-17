import Navbar from "./components/Navbar";
import Quiz from "./components/Quiz";

const mockResponse = {
  metadata: {
    topic: "graphs bfs dfs",
    no_of_questions: 2,
    total_marks: 4,
    minimum_marks: 2,
    message: ""
  },
  q1: {
    question: "What does BFS stand for?",
    options: {
      a: "Binary First Search",
      b: "Breadth First Search",
      c: "Best First Search",
      d: "Balanced First Search"
    },
    correct_answer: { b: "Breadth First Search" },
    marks: 2
  },
  q2: {
    question: "DFS uses which data structure?",
    options: {
      a: "Queue",
      b: "Array",
      c: "Stack",
      d: "Heap"
    },
    correct_answer: { c: "Stack" },
    marks: 2
  }
};

export default function App() {
  return (
    <>
      <Navbar />
      <Quiz data={mockResponse} />;
    </>

  )
}
