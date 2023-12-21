/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class tComponente extends Component {
    setup() {
        this.state = useState({
            resena: {name: "", resena_id: "", puntuacion: "", comentarios: ""},
            resenaList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upobarber.resena"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllResenas()
        })
    }

    async getAllResenas() {
        this.state.resenaList = await this.orm.searchRead(this.model, [], ["name", "resena_id", "puntuacion", "comentarios"])
    }

    addResena() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editResena(resena) {
        this.state.activeId = resena.id
        this.state.isEdit = true
        this.state.task = {...resena}
    }

    async saveResena() {

        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.resena])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.resena)
        }
        $('#exampleModal').modal('hide')
        this.resetForm()
        await this.getAllResenas()
    }

    resetForm() {
        this.state.task = {name: "", resena_id: "", puntuacion: "", comentarios: ""}
    }

}
tComponente.template = 'owl.tComponente';
registry.category('actions').add('owl.action_tComponente_js', tComponente);