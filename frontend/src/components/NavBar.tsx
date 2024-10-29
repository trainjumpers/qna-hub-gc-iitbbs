import { CSSProperties, FunctionComponent } from "react";
import { Container, Nav, Navbar } from "react-bootstrap";
import { NavLink } from "react-router-dom";

interface NavBarProps {}

const NavBar: FunctionComponent<NavBarProps> = () => {
    const activeStyle: CSSProperties = {
        backgroundColor: "white",
        color: "black",
    };

    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="#home">
                    <img
                        alt=""
                        src="/logo.ico"
                        width="30"
                        height="30"
                        className="d-inline-block align-top"
                    />{" "}
                    GC Forums
                </Navbar.Brand>
                <Nav className="justify-content-end" variant="pills">
                    <Nav.Item className="mx-1">
                        <NavLink
                            className="navlink"
                            to="/"
                            style={({ isActive }) =>
                                isActive ? activeStyle : {}
                            }
                        >
                            Home
                        </NavLink>
                    </Nav.Item>
                    <Nav.Item className="mx-1">
                        <NavLink
                            className="navlink"
                            to="/login"
                            style={({ isActive }) =>
                                isActive ? activeStyle : {}
                            }
                        >
                            Login
                        </NavLink>
                    </Nav.Item>
                </Nav>
            </Container>
        </Navbar>
    );
};

export default NavBar;
