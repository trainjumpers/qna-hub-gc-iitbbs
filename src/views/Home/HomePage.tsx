import { FunctionComponent } from "react";
import { Card } from "react-bootstrap";
import { FaComment, FaArrowUp, FaArrowDown } from "react-icons/fa";

interface HomePageProps {}

const HomePage: FunctionComponent<HomePageProps> = () => {
    return (
        <div>
            <Card>
                <div style={{display: "flex", flexDirection: "row"}}>
                    <div style={{marginRight: '10px', marginLeft: "10px"}}>
                        <FaArrowUp/>
                        <div>45</div>
                        <FaArrowDown/>
                    </div>
                <Card.Body>
                    <h2>Question</h2>
                    <Card.Text>
                        Some quick example text to build on the card title and
                        make up the bulk of the card's content.
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
                            <Card.Text>
                                Posted by
                            </Card.Text>
                        </div>
                        <div
                            style={{
                                flexDirection: "row",
                                display: "flex",
                                alignItems: "center",
                            }}
                        >
                            <Card.Text style={{ color: "grey" }}>
                                Posted at
                            </Card.Text>
                        </div>

                        <div
                            style={{
                                flexDirection: "row",
                                display: "flex",
                                alignItems: "center",
                            }}
                        >
                            <FaComment style={{ margin: "5px" }} />
                            <Card.Text>45</Card.Text>
                        </div>
                    </span>
                </Card.Body>
                </div>
            </Card>
        </div>
    );
};

export default HomePage;
