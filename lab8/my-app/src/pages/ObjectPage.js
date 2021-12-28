import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";
import FooterComp from "../components/FooterComp.js";


function ObjectPage(params) {
    const ITCompaniesList = params.location.data
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>IT-компания {ITCompaniesList.name_company}</h2>
            <h4>Специализация компании:</h4>
            <p>{ITCompaniesList.specialization}</p>
            <p><b>Год основания: </b>{ITCompaniesList.foundation_year}</p>
            <Link to="/list"><button>Назад</button></Link>
            <FooterComp></FooterComp>
        </div>
    );
}

export default ObjectPage;