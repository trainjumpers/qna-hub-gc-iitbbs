import { FunctionComponent } from "react";
import CardComponent from "../../components/Card";

interface HomePageProps {}

const HomePage: FunctionComponent<HomePageProps> = () => {
    return (
        <div>
            <CardComponent
                title="Question"
                body="What is the best way to learn React?"
                votes={10}
                comments={2}
                created_by="John Doe"
                created_at="2020-01-01"
            />
        </div>
    );
};

export default HomePage;
