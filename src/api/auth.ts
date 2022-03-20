import axios from "axios";
import { toast } from "react-toastify";
import Cookies from 'universal-cookie';
const cookies = new Cookies();

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
        if (loginResponse.status === 200) {
            cookies.set("access-token", loginResponse.data.access_token);
            toast("Successfully logged in!");
            return true;
        }
    } catch (e: any) {
        toast(e.response.data.message);
        return false;
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
        if (signupResponse.status === 200) {
            toast("Successfully registered!");
        }
    } catch (e: any) {
        toast(e.response.data.message);
    }
};
