import { Dispatch, FunctionComponent, SetStateAction, useState } from "react";
import { Button, Form, Modal } from "react-bootstrap";

interface CreateQuestionModalProps {
    show: boolean;
    setShow: Dispatch<SetStateAction<boolean>>;
    onSave: (title: string, body: string) => void
}

const CreateQuestionModal: FunctionComponent<CreateQuestionModalProps> = (
    props
) => {
    const [title, setTitle] = useState<string>("");
    const [body, setBody] = useState<string>("");

    return (
        <Modal show={props.show} onHide={() => props.setShow(false)}>
            <Modal.Header closeButton>
                <Modal.Title>Post a Question</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group className="mb-3 ps-3" controlId="#">
                        <Form.Label column>Title:</Form.Label>
                        <Form.Control
                            value={title}
                            onChange={(e) => {setTitle(e.target.value)}}
                            type="text"
                            placeholder="Enter Title"
                        />
                        <Form.Label column>Body:</Form.Label>
                        <Form.Control
                            as="textarea"
                            value={body}
                            onChange={(e) => {setBody(e.target.value)}}
                            type="text"
                            placeholder="Enter Body"
                        />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button
                    variant="primary"
                    onClick={() => {
                        props.setShow(false);
                    }}
                >
                    Close
                </Button>
                <Button
                    variant="primary"
                    onClick={() => {
                        props.onSave(title, body);
                    }}
                >
                    Save Changes
                </Button>
            </Modal.Footer>
        </Modal>
    );
};

export default CreateQuestionModal;
