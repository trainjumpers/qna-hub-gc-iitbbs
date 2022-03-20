import {
    createContext,
    Dispatch,
    ReactNode,
    SetStateAction,
    useState,
} from "react";

type TProps = {
    children: ReactNode;
};

export type TAppContext = {
    name: string;
    email: string;
    setName: Dispatch<SetStateAction<string>>;
    setEmail: Dispatch<SetStateAction<string>>;
};

const initialContext: TAppContext = {
    name: "USER",
    email: "",
    setName: (): void => {},
    setEmail: (): void => {},
};

export const AppContext = createContext<TAppContext>(initialContext);

export const AppContextProvider = ({ children }: TProps): JSX.Element => {
    const [name, setName] = useState<string>(initialContext.name);
    const [email, setEmail] = useState<string>(initialContext.email);

    return (
        <AppContext.Provider
            value={{
                name,
                setName,
                email,
                setEmail,
            }}
        >
            {children}
        </AppContext.Provider>
    );
};
