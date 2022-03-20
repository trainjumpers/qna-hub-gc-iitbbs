import axios from "axios";
import { toast } from "react-toastify";

const baseURL = process.env.REACT_APP_BASE_URL;

export const createQuestion = async ( accessToken: string, title: string, body: string) => {
    try {
        const loginResponse = await axios.post<any>(
            `${baseURL}/api/questions`,
            {
                title: title,
                body: body,
            },
            {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Accept: "application/json",
                    Authorization: `Bearer ${accessToken}`,
                },
            }
        );
        toast("Successfully logged in!");
        if(loginResponse.status === 200) {
            return loginResponse.data;
        }
    } catch (e: any) {
        toast(e.response.data.message);
    }
};

