export class ITCompanyCardComponent {
    constructor(parent) {
        this.parent = parent
    }

    getHTML(data) {
        return (
            `
            <div class='card text-white text-center bg-dark'>
                <div class='card-body'>
                    <h4 class='card-title'>${data.name_company}</h4>
                    <!--<p class='card-text'>${data.specialization}</p>-->
                    <!--<p class='card-text'>${data.foundation_year}</p>-->
                    <button class='btn btn-primary', id='click-card-${data.id_company}', data-id='${data.id_company}'>Подробнее</button>
                </div>
            </div>
            `
        )
    }

    addListeners(data, listener) {
        console.log(document.getElementById(`click-card-${data.id_company}`))
        document.getElementById(`click-card-${data.id_company}`).addEventListener('click', listener)
    }

    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
}