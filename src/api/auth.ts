import axios from "axios";
import { toast } from "react-toastify";

const baseURL = process.env.REACT_APP_BASE_URL;

export const handleLogin = async (username: string, password: string) => {
    try {
        const loginResponse = await axios.post<any>(
            `${baseURL}/api/users/login`,
            `username=${username}&password=${password}`,
            {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Accept: "application/json",
                },
            }
        );
        toast("Successfully logged in!");
    } catch (e: any) {
        toast(e.response.data.message);
    }
};

export const handleSignup = async (email: string, password: string) => {
    try {
        const signupResponse = await axios.post<any>(
            `${baseURL}/api/users/signup`,
            {
                email: email,
                password: password,
            },

            {
                headers: {
                    Accept: "application/json",
                },
            }
        );
        toast("Successfully registered!");
    } catch (e: any) {
        toast(e.response.data.message);
    }
};
