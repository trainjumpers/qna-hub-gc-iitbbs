import { FunctionComponent, useEffect } from "react";
import { Button } from "react-bootstrap";
import { createQuestion, fetchQuestions } from "../../api/question";
import CardComponent from "../../components/Card";

interface HomePageProps {}

const HomePage: FunctionComponent<HomePageProps> = () => {

    useEffect(() => {
      fetchQuestions();
    }, [])
    

    const handleCreateQuestion = () => {
        console.log("Create Question");
        createQuestion("Test Question", "Test Body");
    }

    return (
        <div>
            <Button style={{margin: "10px"}} onClick={handleCreateQuestion}>Create Question</Button>
            <CardComponent
                title="Question"
                body="What is the best way to learn React?"
                votes={10}
                comments={2}
                created_by="John Doe"
                created_at="2020-01-01"
            />
        </div>
    );
};

export default HomePage;
