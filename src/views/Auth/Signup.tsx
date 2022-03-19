import { FunctionComponent } from "react";
import { Button, Card, Container, Form } from "react-bootstrap";
import { Link } from "react-router-dom";

interface SignUpScreenProps {}

const SignUpScreen: FunctionComponent<SignUpScreenProps> = () => {
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
                            />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="password">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                type="password"
                                placeholder="Password"
                            />
                        </Form.Group>
                        <Button variant="primary">
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
