export class ITCompanyComponent {
    constructor(parent) {
        this.parent = parent
    }

    getHTML(data) {
        return (
            `
            <div class='card text-white bg-dark' style='width: 300px'>
                <div class="card-header">
                    IT-компания
                </div>
                <div class='card-body'>
                    <h4 class='card-title'>${data.name_company}</h4>
                    <p class='card-text'>${data.specialization}</p>
                    <p class='card-text'>Год основания: ${data.foundation_year}</p>
                </div>
            </div>
            `
        )
    }

    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
    }
}