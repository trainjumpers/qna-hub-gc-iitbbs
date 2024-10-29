import axios from "axios";
import { toast } from "react-toastify";
import Cookies from "universal-cookie";
const cookies = new Cookies();

const baseURL = process.env.REACT_APP_BASE_URL;

export const createQuestion = async (title: string, body: string) => {
    try {
        const createQuestionResponse = await axios.post<any>(
            `${baseURL}/api/questions`,
            {
                title: title,
                body: body,
            },
            {
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                    Authorization: `Bearer ${cookies.get("access-token")}`,
                },
            }
        );
        if (createQuestionResponse.status === 201) {
            console.log(createQuestionResponse.data)
            return createQuestionResponse.data;
        }
    } catch (e: any) {
        toast(e.response.data.message);
        return;
    }
};

export const fetchQuestions = async () => {
    try {
        const fetchQuestionsResponse = await axios.get<any>(
            `${baseURL}/api/questions`,
            {
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                    Authorization: `Bearer ${cookies.get("access-token")}`,
                },
            }
        );
        if (fetchQuestionsResponse.status === 200) {
            return fetchQuestionsResponse.data;
        }
    } catch (e: any) {
        toast(e.response.data.message);
        return;
    }
};
