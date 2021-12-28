const getObjects = async () =>{
    const res = await fetch('http://127.0.0.1:8000/it_company/', {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(()=>{
            return {resultCount:0, results:[]}
        })
    return res
}

export default getObjects