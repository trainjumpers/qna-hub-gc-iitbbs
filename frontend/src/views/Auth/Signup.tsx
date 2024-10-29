import { FunctionComponent, useState } from "react";
import { Button, Card, Container, Form } from "react-bootstrap";
import { Link } from "react-router-dom";
import { handleSignup } from "../../api/auth";
import { useNavigate } from "react-router-dom";

interface SignUpScreenProps {}

const SignUpScreen: FunctionComponent<SignUpScreenProps> = () => {
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const navigate = useNavigate();

    const signup = async () => {
        const success = await handleSignup(email, password);
        if (!success) return;
        navigate("/");
    };

    return (
        <Container className="mt-5">
            <Card style={{ width: "45rem" }} className="mx-auto">
                <Card.Header>
                    <Card.Title>Register as a new User</Card.Title>
                </Card.Header>
                <Card.Body>
                    <Form>
                        <Form.Group className="mb-3" controlId="email">
                            <Form.Label>Email address</Form.Label>
                            <Form.Control
                                type="email"
                                placeholder="Enter email"
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="password">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                type="password"
                                placeholder="Password"
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </Form.Group>
                        <Button variant="primary" onClick={signup}>
                            Signup
                        </Button>
                    </Form>
                </Card.Body>
                <Card.Footer>
                    <Form.Label>
                        Already an existing User? Log in{" "}
                        <Link to="/login">here</Link>
                    </Form.Label>
                </Card.Footer>
            </Card>
        </Container>
    );
};

export default SignUpScreen;
