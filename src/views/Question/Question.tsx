import { FunctionComponent } from "react";
import { Card, Container } from "react-bootstrap";
import { FaArrowDown, FaArrowUp } from "react-icons/fa";
import CardComponent from "../../components/Card";
import { useLocation } from "react-router-dom";

interface QuestionProps {}

const Question: FunctionComponent<QuestionProps> = () => {
    const { state } = useLocation();
    const question: any = state;
    return (
        <Container>
            <CardComponent
                className="mt-4"
                title={question.title}
                body={question.body}
                votes={question.upvotes - question.downvotes}
                // comments={2}
                created_by={question.created_by}
                created_at={question.created_at}
            />
            <Card className="mt-3">
                <Card.Header>
                    <Card.Title>
                        <h2>Discussion:</h2>
                    </Card.Title>
                </Card.Header>
                <div>
                    <Card>
                        <div style={{ display: "flex", flexDirection: "row" }}>
                            <div
                                style={{
                                    marginRight: "10px",
                                    marginLeft: "10px",
                                }}
                            >
                                <FaArrowUp />
                                <div>10</div>
                                <FaArrowDown />
                            </div>
                            <Card.Body>
                                <h2>Answer</h2>
                                <Card.Text>
                                    What is the best way to learn React?
                                </Card.Text>
                                <hr></hr>
                                <span
                                    style={{
                                        flexDirection: "row",
                                        display: "flex",
                                        justifyContent: "space-between",
                                    }}
                                >
                                    <div
                                        style={{
                                            flexDirection: "row",
                                            display: "flex",
                                            alignItems: "center",
                                        }}
                                    >
                                        <Card.Text>Posted by: og118</Card.Text>
                                    </div>
                                    <div
                                        style={{
                                            flexDirection: "row",
                                            display: "flex",
                                            alignItems: "center",
                                        }}
                                    >
                                        <Card.Text style={{ color: "grey" }}>
                                            Posted at: now
                                        </Card.Text>
                                    </div>
                                </span>
                            </Card.Body>
                        </div>
                    </Card>
                    <Card>
                        <div style={{ display: "flex", flexDirection: "row" }}>
                            <div
                                style={{
                                    marginRight: "10px",
                                    marginLeft: "10px",
                                }}
                            >
                                <FaArrowUp />
                                <div>10</div>
                                <FaArrowDown />
                            </div>
                            <Card.Body>
                                <h2>Answer</h2>
                                <Card.Text>
                                    What is the best way to learn React?
                                </Card.Text>
                                <hr></hr>
                                <span
                                    style={{
                                        flexDirection: "row",
                                        display: "flex",
                                        justifyContent: "space-between",
                                    }}
                                >
                                    <div
                                        style={{
                                            flexDirection: "row",
                                            display: "flex",
                                            alignItems: "center",
                                        }}
                                    >
                                        <Card.Text>Posted by: og118</Card.Text>
                                    </div>
                                    <div
                                        style={{
                                            flexDirection: "row",
                                            display: "flex",
                                            alignItems: "center",
                                        }}
                                    >
                                        <Card.Text style={{ color: "grey" }}>
                                            Posted at: now
                                        </Card.Text>
                                    </div>
                                </span>
                            </Card.Body>
                        </div>
                    </Card>
                </div>
            </Card>
        </Container>
    );
};

export default Question;
