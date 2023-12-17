/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class cComponente extends Component {
    setup() {
        this.state = useState({
            cliente: { name: "", nombre: "", apellidos: "", correoElectronico: "" },
            clienteList: [],
            isEdit: false,
            activeId: false,
        });
        this.orm = useService("orm");
        this.model = "upobarber.cliente";  
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllClientes();
        });
    }

    async getAllClientes() {
        this.state.clienteList = await this.orm.searchRead(this.model, [], ["name", "nombre", "apellidos", "correoElectronico"]);
    }

    addCliente() {
        this.resetForm();
        this.state.activeId = false;
        this.state.isEdit = false;
    }

    editCliente(cliente) {
        this.state.activeId = cliente.id;
        this.state.isEdit = true;
        this.state.cliente = { ...cliente };
    }

    async saveCliente() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.cliente]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.cliente);
        }
        $('#exampleModal').modal('hide');
        this.resetForm();
        await this.getAllClientes();
    }

    resetForm() {
        this.state.cliente = { name: "", nombre: "", apellidos: "", correoElectronico: "" };
    }

}

cComponente.template = 'owl.cComponente';
registry.category('actions').add('owl.action_cComponente_js', cComponente);