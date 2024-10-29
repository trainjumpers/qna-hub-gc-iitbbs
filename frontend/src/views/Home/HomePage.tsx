import { FunctionComponent, useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import Cookies from "universal-cookie";
import { createQuestion, fetchQuestions } from "../../api/question";
import CardComponent from "../../components/Card";
import CreateQuestionModal from "../../components/CreateQuestionModal";

interface HomePageProps {}

const HomePage: FunctionComponent<HomePageProps> = () => {
    const cookies = new Cookies();
    const navigate = useNavigate();
    const [questions, setQuestions] = useState<Array<any>>([]);
    const [showCreateQuestionModal, setShowCreateQuestionModal] =
        useState<boolean>(false);

    const getQuestionData = async () => {
        const questionData = await fetchQuestions();
        if (questionData === null) return;
        console.log(questionData);
        setQuestions(questionData);
    };

    useEffect(() => {
        getQuestionData();
    }, []);

    const handleCreateQuestion = async (title: string, body: string) => {
        const createdQuestion = await createQuestion(title, body);
        if (createdQuestion === null) return;
        setQuestions([...questions, createdQuestion]);
        setShowCreateQuestionModal(false);
    };

    if (cookies.get("access-token") === undefined) {
        navigate("/login");
    }
    return (
        <div>
            <CreateQuestionModal
                show={showCreateQuestionModal}
                setShow={setShowCreateQuestionModal}
                onSave={handleCreateQuestion}
            />
            <Button
                style={{
                    marginTop: "10px",
                    backgroundColor: "black",
                    border: "black",
                    outline: "none",
                }}
                onClick={() => setShowCreateQuestionModal(true)}
            >
                Create Question
            </Button>
            {questions.map((question) => (
                <CardComponent
                    onClick={() =>
                        navigate(`/question/${question.id}`, {
                            state: question,
                        })
                    }
                    className="mt-2"
                    title={question.title}
                    body={question.body}
                    votes={question.upvotes - question.downvotes}
                    // comments={5}
                    created_by={question.created_by}
                    created_at={question.created_at}
                    style={{ cursor: "pointer" }}
                />
            ))}
        </div>
    );
};

export default HomePage;
