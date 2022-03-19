import { FunctionComponent, useState } from "react";
import { Button, Card, Container, Form } from "react-bootstrap";
import { Link } from "react-router-dom";
import { handleLogin } from "../../api/auth";

interface LoginScreenProps {}

const LoginScreen: FunctionComponent<LoginScreenProps> = () => {
const [email, setEmail] = useState<string>("")
const [password, setPassword] = useState<string>("")

    return (
        <Container className="mt-5">
            <Card style={{width: "45rem"}} className="mx-auto">
                <Card.Header>
                    <Card.Title>Login to your Account</Card.Title>
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
                        <Button variant="primary" onClick={() => {
                            console.log(email, password)
                            handleLogin(email, password)
                        }}>
                            Login
                        </Button>
                    </Form>
                </Card.Body>
                <Card.Footer>
                    <Form.Label>
                        Don't have an account? Register{" "}
                        <Link to="/signup">here</Link>
                    </Form.Label>
                </Card.Footer>
            </Card>
        </Container>
    );
};

export default LoginScreen;
