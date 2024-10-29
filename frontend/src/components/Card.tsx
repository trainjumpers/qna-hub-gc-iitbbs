import { CSSProperties, FunctionComponent } from "react";
import { Card } from "react-bootstrap";
import { FaComment, FaArrowUp, FaArrowDown } from "react-icons/fa";

type CardProps = {
    className?: string;
    onClick?: () => void;
    style?: CSSProperties;
    title: string;
    body?: string;
    votes: number;
    // comments: number;
    created_by: string;
    created_at: string;
};

const CardComponent: FunctionComponent<CardProps> = (props: CardProps) => {
    const upvote = () => {};
    const downvote = () => {};

    return (
        <div>
            <Card
                className={props.className}
                onClick={props.onClick}
                style={props.style}
            >
                <div style={{ display: "flex", flexDirection: "row" }}>
                    <div style={{ marginRight: "10px", marginLeft: "10px" }}>
                        <FaArrowUp onClick={upvote}/>
                        <div>{props.votes}</div>
                        <FaArrowDown onClick={downvote}/>
                    </div>
                    <Card.Body>
                        <h2>{props.title}</h2>
                        <Card.Text>{props.body}</Card.Text>
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
                                    Posted by: {props.created_by}
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
                                    Posted at: {props.created_at}
                                </Card.Text>
                            </div>

                            <div
                                style={{
                                    flexDirection: "row",
                                    display: "flex",
                                    alignItems: "center",
                                }}
                            >
                                {/* <FaComment style={{ margin: "5px" }} /> */}
                                {/* <Card.Text>{props.comments}</Card.Text> */}
                            </div>
                        </span>
                    </Card.Body>
                </div>
            </Card>
        </div>
    );
};

export default CardComponent;
