class Urls {
    constructor() {
        this.url = 'http://localhost:8000/';
    }

    IT_Companies() {
        return `${this.url}it_company/`
    }

    IT_Company(id) {
        return `${this.url}it_company/${id}/`
    }
}

export const urls = new Urls()