/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class jaComponente extends Component {
    setup() {
        this.state = useState({
            pago:{name:"", pagado:"", metodo_id:"", concepto:""},
            pagoList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upobarber.pago"
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllPagos()
        })
    }

    async getAllPagos(){
        this.state.pagoList = await this.orm.searchRead(this.model, [], ["name", "pagado", "metodo_id", "concepto"])
    }

    addPago(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editPago(pago){
        this.state.activeId = pago.id
        this.state.isEdit = true
        this.state.pago = {...pago}
    }

    async savePago(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.pago])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.pago)
        }
        $('#exampleModal').modal('hide')
        this.resetForm()
        await this.getAllPagos()
    }

    resetForm(){
        this.state.pago = {name:"", pagado:"", metodo_id:"", concepto:""}
    }

    async deletePago(pago){
        await this.orm.unlink(this.model, [pago.id])
        await this.getAllPagos()
    }

    async searchPagos(){
        const text = this.searchInput.el.value
        this.state.pagoList = await this.orm.searchRead(this.model, [['name','ilike',text]], ["name", "pagado", "metodo_id", "concepto"])
    }
  
}
    
jaComponente.template = 'owl.jaComponente';
registry.category('actions').add('owl.action_jaComponente_js', jaComponente);