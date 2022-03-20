import { Routes, Route, Link, NavLink } from "react-router-dom";
import Container from "react-bootstrap/Container";

import LoginScreen from "./views/Auth/Login";
import SignUpScreen from "./views/Auth/Signup";
import VerifyEmailScreen from "./views/Auth/VerifyEmail";
import HomePage from "./views/Home/HomePage";
import { Nav, Navbar } from "react-bootstrap";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import "./App.css";

function App() {
    const activeStyle = {
        backgroundColor: "white",
        color: "black"
    }

    return (
        <div>
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
            <Container>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/login" element={<LoginScreen />}></Route>
                    <Route path="/signup" element={<SignUpScreen />}></Route>
                    <Route
                        path="/verify"
                        element={<VerifyEmailScreen />}
                    ></Route>
                </Routes>
            </Container>
            <ToastContainer />
        </div>
    );
}

export default App;
