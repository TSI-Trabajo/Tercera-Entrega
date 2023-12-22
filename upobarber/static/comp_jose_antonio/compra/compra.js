/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class jaComponente extends Component {
    setup() {
        this.state = useState({
            compra:{name:"", importe:"", fechaCompra:"", pago_id:"", articulo_id:""},
            compraList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upobarber.compra"
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllCompras()
        })
    }

    async getAllCompras(){
        this.state.compraList = await this.orm.searchRead(this.model, [], ["name", "importe", "fechaCompra", "pago_id", "articulo_id"])
    }

    addCompra(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editCompra(compra){
        this.state.activeId = compra.id
        this.state.isEdit = true
        this.state.compra = {...compra}
    }

    async saveCompra(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.compra])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.compra)
        }
        $('#exampleModal').modal('hide')
        this.resetForm()
        await this.getAllCompras()
    }

    resetForm(){
        this.state.compra = {name:"", importe:"", fechaCompra:"", pago_id:"", articulo_id:""}
    }

    async deleteCompra(compra){
        await this.orm.unlink(this.model, [compra.id])
        await this.getAllCompras()
    }

    async searchCompras(){
        const text = this.searchInput.el.value
        this.state.compraList = await this.orm.searchRead(this.model, [['name','ilike',text]], ["name", "importe", "fechaCompra", "pago_id", "articulo_id"])
    }
  
}
    
jaComponente.template = 'owl.jaComponente';
registry.category('actions').add('owl.action_jaComponente_js', jaComponente);