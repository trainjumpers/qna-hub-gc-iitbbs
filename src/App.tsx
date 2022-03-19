import { Routes, Route } from "react-router-dom";
import LoginScreen from "./views/Auth/Login";
import SignUpScreen from "./views/Auth/Signup";
import VerifyEmailScreen from "./views/Auth/VerifyEmail";
import HomePage from "./views/Home/HomePage";

function App() {
    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginScreen />}></Route>
            <Route path="/signup" element={<SignUpScreen />}></Route>
            <Route path="/verify" element={<VerifyEmailScreen />}></Route>
        </Routes>
    );
}

export default App;
