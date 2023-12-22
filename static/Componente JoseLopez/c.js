/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class cComponente extends Component {
    setup() {
        this.state = useState({
            empleado: { name: "", nombre: "", apellidos: "", correoElectronico: "" },
            empleadoList: [],
            isEdit: false,
            activeId: false,
        });
        this.orm = useService("orm");
        this.model = "upobarber.empleado";  
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllEmpleados();
        });
    }

    async getAllEmpleados() {
        this.state.empleadoList = await this.orm.searchRead(this.model, [], ["name", "nombre", "apellidos", "correoElectronico"]);
    }

    addempleado() {
        this.resetForm();
        this.state.activeId = false;
        this.state.isEdit = false;
    }

    editEmpleado(empleado) {
        this.state.activeId = empleado.id;
        this.state.isEdit = true;
        this.state.empleado = { ...empleado };
    }

    async saveempleado() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.empleado]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.empleado);
        }
        $('#exampleModal').modal('hide');
        this.resetForm();
        await this.getAllEmpleados();
    }

    resetForm() {
        this.state.empleado = { name: "", nombre: "", apellidos: "", correoElectronico: "" };
    }

}

cComponente.template = 'owl.cComponente';
registry.category('actions').add('owl.action_cComponente_js', cComponente);