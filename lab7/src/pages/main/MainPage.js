import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";
import {ITCompanyPage} from "../IT_Company/ITCompanyPage.js";
import {ITCompanyCardComponent} from "../../components/IT_company/ITCompanyCardComponent.js";

export class MainPage {
    constructor(parent) {
        this.parent = parent
    }

    async getData() {
        return ajax.get(urls.IT_Companies())
    }

    page() {
        return document.getElementById('main-page')
    }

    getHTML() {
        return '<div id="main-page" class="d-flex flex-wrap"><div/>'
    }

    clickCard(e) {
        const cardId = e.target.dataset.id
        const itCompanyPage = new ITCompanyPage(this.parent, cardId)
        itCompanyPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const data = await this.getData()
        data.data.forEach((item) => {
            const IT_Company_card = new ITCompanyCardComponent(this.page())
            IT_Company_card.render(item, this.clickCard.bind(this))
        })
    }
}