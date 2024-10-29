import { Routes, Route } from "react-router-dom";
import Container from "react-bootstrap/Container";

import LoginScreen from "./views/Auth/Login";
import SignUpScreen from "./views/Auth/Signup";
import VerifyEmailScreen from "./views/Auth/VerifyEmail";
import HomePage from "./views/Home/HomePage";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import "./App.css";
import NavBar from "./components/NavBar";
import Question from "./views/Question/Question";

function App() {
    return (
        <div>
            <NavBar />
            <Container>
                <Routes>
                    <Route path="/login" element={<LoginScreen />}></Route>
                    <Route path="/signup" element={<SignUpScreen />}></Route>
                    
                    <Route path="/" element={<HomePage />} />
                    <Route path="/question/:id" element={<Question />} />

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
