import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";
import FooterComp from "../components/FooterComp.js";
import getObjects from "../modules/GetObjects.js";


function ListPage() {

    const [ITCompaniesList, setITCompaniesList] = useState([])
    const [ITCompaniesNames, setITCompaniesNames] = useState([])

    const handleObjectsList = async () => {
        const names = []
        const ITCompanies = await getObjects()
        for (let ITCompany of ITCompanies) {
            names.push(ITCompany['name_company']);
        }
        setITCompaniesList(ITCompanies)
        setITCompaniesNames(names)
    }

    useEffect(()=>{
        handleObjectsList()
    }, [])

    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Список объектов таблицы IT-company</h2>
            <ul>
                {ITCompaniesNames.map((name)=>{
                    return (
                        <li key={name}>
                            <Link to={{pathname: "/list/object", data: ITCompaniesList.find(o => o.name_company == name)}}>{name}</Link>
                        </li>
                    )
                })}
            </ul>
            <FooterComp></FooterComp>
        </div>
    );
}

export default ListPage;