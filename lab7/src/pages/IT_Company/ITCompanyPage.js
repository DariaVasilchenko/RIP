import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";
import {MainPage} from "../main/MainPage.js";
import {BackButtonComponent} from "../../components/back-button/BackButtonComponent.js";
import {ITCompanyComponent} from "../../components/IT_company/ITCompanyComponent.js";

export class ITCompanyPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }

    async getData() {
        return ajax.get(urls.IT_Company(this.id))
    }

    page() {
        return document.getElementById('stock-page')
    }

    getHTML() {
        return '<div id="stock-page"></div>'
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const back_button = new BackButtonComponent(this.page())
        back_button.render(this.clickBack.bind(this))

        const data = await this.getData()
        const ITCompany_card = new ITCompanyComponent(this.page())
        ITCompany_card.render(data.data)
    }
}