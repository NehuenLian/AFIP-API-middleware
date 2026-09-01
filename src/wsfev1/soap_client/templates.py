
WSFEV1_TEMPLATE_PROLOGUE = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
"""

WSFEV1_TEMPLATE_EPILOGUE = """    </soapenv:Body>
</soapenv:Envelope>
"""

FEDummy = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEDummy/>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECAESolicitar = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECAESolicitar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:FeCAEReq>
                <ar:FeCabReq>
                    <ar:CantReg>{{ FeCAEReq.FeCabReq.CantReg }}</ar:CantReg>
                    <ar:PtoVta>{{ FeCAEReq.FeCabReq.PtoVta }}</ar:PtoVta>
                    <ar:CbteTipo>{{ FeCAEReq.FeCabReq.CbteTipo }}</ar:CbteTipo>
                </ar:FeCabReq>
                <ar:FeDetReq>
                {% for item in FeCAEReq.FeDetReq.FECAEDetRequest %}
                    <ar:FECAEDetRequest>
                        <ar:Concepto>{{ item.Concepto }}</ar:Concepto>
                        <ar:DocTipo>{{ item.DocTipo }}</ar:DocTipo>
                        <ar:DocNro>{{ item.DocNro }}</ar:DocNro>
                        <ar:CbteDesde>{{ item.CbteDesde }}</ar:CbteDesde>
                        <ar:CbteHasta>{{ item.CbteHasta }}</ar:CbteHasta>
                        <ar:CbteFch>{{ item.CbteFch }}</ar:CbteFch>
                        <ar:ImpTotal>{{ item.ImpTotal }}</ar:ImpTotal>
                        <ar:ImpTotConc>{{ item.ImpTotConc }}</ar:ImpTotConc>
                        <ar:ImpNeto>{{ item.ImpNeto }}</ar:ImpNeto>
                        <ar:ImpOpEx>{{ item.ImpOpEx }}</ar:ImpOpEx>
                        <ar:ImpTrib>{{ item.ImpTrib }}</ar:ImpTrib>
                        <ar:ImpIVA>{{ item.ImpIVA }}</ar:ImpIVA>
                    {% if item.FchServDesde %}
                        <ar:FchServDesde>{{ item.FchServDesde }}</ar:FchServDesde>
                    {% endif %}
                    {% if item.FchServHasta %}
                        <ar:FchServHasta>{{ item.FchServHasta }}</ar:FchServHasta>
                    {% endif %}
                    {% if item.FchVtoPago %}
                        <ar:FchVtoPago>{{ item.FchVtoPago }}</ar:FchVtoPago>
                    {% endif %}
                        <ar:MonId>{{ item.MonId }}</ar:MonId>
                    {% if item.MonCotiz %}
                        <ar:MonCotiz>{{ item.MonCotiz }}</ar:MonCotiz>
                    {% endif %}
                    {% if item.CanMisMonExt %}
                        <ar:CanMisMonExt>{{ item.CanMisMonExt }}</ar:CanMisMonExt>
                    {% endif %}
                        <ar:CondicionIVAReceptorId>{{ item.CondicionIVAReceptorId }}</ar:CondicionIVAReceptorId>

                        {% if item.CbtesAsoc %}
                        <ar:CbtesAsoc>
                            {% for i in item.CbtesAsoc %}
                            <ar:CbteAsoc>
                                <ar:Tipo>{{ i.Tipo }}</ar:Tipo>
                                <ar:PtoVta>{{ i.PtoVta }}</ar:PtoVta>
                                <ar:Nro>{{ i.Nro }}</ar:Nro>
                                <ar:Cuit>{{ i.Cuit }}</ar:Cuit>
                                <ar:CbteFch>{{ i.CbteFch }}</ar:CbteFch>
                            </ar:CbteAsoc>
                            {% endfor %}
                        </ar:CbtesAsoc>
                        {% endif %}

                        {% if item.Tributos %}
                        <ar:Tributos>
                            {% for i in item.Tributos %}
                            <ar:Tributo>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Desc>{{ i.Desc }}</ar:Desc>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Alic>{{ i.Alic }}</ar:Alic>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:Tributo>
                            {% endfor %}
                        </ar:Tributos>
                        {% endif %}

                        {% if item.Iva %}
                        <ar:Iva>
                            {% for i in item.Iva %}
                            <ar:AlicIva>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:AlicIva>
                            {% endfor %}
                        </ar:Iva>
                        {% endif %}

                        {% if item.Opcionales %}
                        <ar:Opcionales>
                            {% for i in item.Opcionales %}
                            <ar:Opcional>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Valor>{{ i.Valor }}</ar:Valor>
                            </ar:Opcional>
                            {% endfor %}
                        </ar:Opcionales>
                        {% endif %}

                        {% if item.Compradores %}
                        <ar:Compradores>
                            {% for i in item.Compradores %}
                            <ar:Comprador>
                                <ar:DocTipo>{{ i.DocTipo }}</ar:DocTipo>
                                <ar:DocNro>{{ i.DocNro }}</ar:DocNro>
                                <ar:Porcentaje>{{ i.Porcentaje }}</ar:Porcentaje>
                            </ar:Comprador>
                            {% endfor %}
                        </ar:Compradores>
                        {% endif %}

                        {% if item.PeriodoAsoc %}
                        <ar:PeriodoAsoc>
                            {% for i in item.PeriodoAsoc %}
                                <ar:FchDesde>{{ i.FchDesde }}</ar:FchDesde>
                                <ar:FchHasta>{{ i.FchHasta }}</ar:FchHasta>
                            {% endfor %}
                        </ar:PeriodoAsoc>
                        {% endif %}

                        {% if item.Actividades %}
                        <ar:Actividades>
                            {% for i in item.Actividades %}
                            <ar:Actividad>
                                <ar:Id>{{ i.Id }}</ar:Id>
                            </ar:Actividad>
                            {% endfor %}
                        </ar:Actividades>
                        {% endif %}

                    </ar:FECAEDetRequest>
                    {% endfor %}
                </ar:FeDetReq>
            </ar:FeCAEReq>
        </ar:FECAESolicitar>
    </soapenv:Body>
</soapenv:Envelope>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECompTotXRequest = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECompTotXRequest>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FECompTotXRequest>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECompUltimoAutorizado = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECompUltimoAutorizado>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:PtoVta>{{ PtoVta }}</ar:PtoVta>
            <ar:CbteTipo>{{ CbteTipo }}</ar:CbteTipo>
        </ar:FECompUltimoAutorizado>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECompConsultar = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECompConsultar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:FeCompConsReq>
                <ar:CbteTipo>{{ FeCompConsReq.CbteTipo }}</ar:CbteTipo>
                <ar:CbteNro>{{ FeCompConsReq.CbteNro }}</ar:CbteNro>
                <ar:PtoVta>{{ FeCompConsReq.PtoVta }}</ar:PtoVta>
            </ar:FeCompConsReq>
        </ar:FECompConsultar>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECAEARegInformativo = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECAEARegInformativo>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:FeCAEARegInfReq>
                <ar:FeCabReq>
                    <ar:CantReg>{{ FeCAEARegInfReq.FeCabReq.CantReg }}</ar:CantReg>
                    <ar:PtoVta>{{ FeCAEARegInfReq.FeCabReq.PtoVta }}</ar:PtoVta>
                    <ar:CbteTipo>{{ FeCAEARegInfReq.FeCabReq.CbteTipo }}</ar:CbteTipo>
                </ar:FeCabReq>
                <ar:FeDetReq>
                {% for item in FeCAEARegInfReq.FeDetReq.FECAEADetRequest %}
                    <ar:FECAEADetRequest>
                        <ar:Concepto>{{ item.Concepto }}</ar:Concepto>
                        <ar:DocTipo>{{ item.DocTipo }}</ar:DocTipo>
                        <ar:DocNro>{{ item.DocNro }}</ar:DocNro>
                        <ar:CbteDesde>{{ item.CbteDesde }}</ar:CbteDesde>
                        <ar:CbteHasta>{{ item.CbteHasta }}</ar:CbteHasta>
                        <ar:CbteFch>{{ item.CbteFch }}</ar:CbteFch>
                        <ar:ImpTotal>{{ item.ImpTotal }}</ar:ImpTotal>
                        <ar:ImpTotConc>{{ item.ImpTotConc }}</ar:ImpTotConc>
                        <ar:ImpNeto>{{ item.ImpNeto }}</ar:ImpNeto>
                        <ar:ImpOpEx>{{ item.ImpOpEx }}</ar:ImpOpEx>
                        <ar:ImpTrib>{{ item.ImpTrib }}</ar:ImpTrib>
                        <ar:ImpIVA>{{ item.ImpIVA }}</ar:ImpIVA>
                    {% if item.FchServDesde %}
                        <ar:FchServDesde>{{ item.FchServDesde }}</ar:FchServDesde>
                    {% endif %}
                    {% if item.FchServHasta %}
                        <ar:FchServHasta>{{ item.FchServHasta }}</ar:FchServHasta>
                    {% endif %}
                    {% if item.FchVtoPago %}
                        <ar:FchVtoPago>{{ item.FchVtoPago }}</ar:FchVtoPago>
                    {% endif %}
                        <ar:MonId>{{ item.MonId }}</ar:MonId>
                    {% if item.MonCotiz %}
                        <ar:MonCotiz>{{ item.MonCotiz }}</ar:MonCotiz>
                    {% endif %}
                    {% if item.CanMisMonExt %}
                        <ar:CanMisMonExt>{{ item.CanMisMonExt }}</ar:CanMisMonExt>
                    {% endif %}
                        <ar:CondicionIVAReceptorId>{{ item.CondicionIVAReceptorId }}</ar:CondicionIVAReceptorId>

                        {% if item.CbtesAsoc %}
                        <ar:CbtesAsoc>
                            {% for i in item.CbtesAsoc %}
                            <ar:CbteAsoc>
                                <ar:Tipo>{{ i.Tipo }}</ar:Tipo>
                                <ar:PtoVta>{{ i.PtoVta }}</ar:PtoVta>
                                <ar:Nro>{{ i.Nro }}</ar:Nro>
                                <ar:Cuit>{{ i.Cuit }}</ar:Cuit>
                                <ar:CbteFch>{{ i.CbteFch }}</ar:CbteFch>
                            </ar:CbteAsoc>
                            {% endfor %}
                        </ar:CbtesAsoc>
                        {% endif %}

                        {% if item.Tributos %}
                        <ar:Tributos>
                            {% for i in item.Tributos %}
                            <ar:Tributo>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Desc>{{ i.Desc }}</ar:Desc>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Alic>{{ i.Alic }}</ar:Alic>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:Tributo>
                            {% endfor %}
                        </ar:Tributos>
                        {% endif %}

                        {% if item.Iva %}
                        <ar:Iva>
                            {% for i in item.Iva %}
                            <ar:AlicIva>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:AlicIva>
                            {% endfor %}
                        </ar:Iva>
                        {% endif %}

                        {% if item.Opcionales %}
                        <ar:Opcionales>
                            {% for i in item.Opcionales %}
                            <ar:Opcional>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Valor>{{ i.Valor }}</ar:Valor>
                            </ar:Opcional>
                            {% endfor %}
                        </ar:Opcionales>
                        {% endif %}

                        {% if item.Compradores %}
                        <ar:Compradores>
                            {% for i in item.Compradores %}
                            <ar:Comprador>
                                <ar:DocTipo>{{ i.DocTipo }}</ar:DocTipo>
                                <ar:DocNro>{{ i.DocNro }}</ar:DocNro>
                                <ar:Porcentaje>{{ i.Porcentaje }}</ar:Porcentaje>
                            </ar:Comprador>
                            {% endfor %}
                        </ar:Compradores>
                        {% endif %}

                        <ar:CAEA>{{ item.CAEA }}</ar:CAEA>

                        {% if item.CbteFchHsGen %}
                            <ar:CbteFchHsGen>{{ item.CbteFchHsGen }}</ar:CbteFchHsGen>
                        {% endif %}

                        {% if item.PeriodoAsoc %}
                        <ar:PeriodoAsoc>
                            {% for i in item.PeriodoAsoc %}
                                <ar:FchDesde>{{ i.FchDesde }}</ar:FchDesde>
                                <ar:FchHasta>{{ i.FchHasta }}</ar:FchHasta>
                            {% endfor %}
                        </ar:PeriodoAsoc>
                        {% endif %}

                        {% if item.Actividades %}
                        <ar:Actividades>
                            {% for i in item.Actividades %}
                            <ar:Actividad>
                                <ar:Id>{{ i.Id }}</ar:Id>
                            </ar:Actividad>
                            {% endfor %}
                        </ar:Actividades>
                        {% endif %}

                    </ar:FECAEADetRequest>
                    {% endfor %}
                </ar:FeDetReq>
            </ar:FeCAEARegInfReq>
        </ar:FECAEARegInformativo>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECAEASolicitar = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECAEASolicitar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:Periodo>{{ Periodo }}</ar:Periodo>
            <ar:Orden>{{ Orden }}</ar:Orden>
        </ar:FECAEASolicitar>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECAEASinMovimientoConsultar = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECAEASinMovimientoConsultar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:CAEA>{{ CAEA }}</ar:CAEA>
            <ar:PtoVta>{{ PtoVta }}</ar:PtoVta>
        </ar:FECAEASinMovimientoConsultar>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECAEASinMovimientoInformar = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECAEASinMovimientoInformar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:PtoVta>{{ PtoVta }}</ar:PtoVta>
            <ar:CAEA>{{ CAEA }}</ar:CAEA>
        </ar:FECAEASinMovimientoInformar>
""" + WSFEV1_TEMPLATE_EPILOGUE

FECAEAConsultar = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FECAEAConsultar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
                <ar:Periodo>{{ Periodo }}</ar:Periodo>
                <ar:Orden>{{ Orden }}</ar:Orden>
        </ar:FECAEAConsultar>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetCotizacion = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetCotizacion>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
                <ar:MonId>{{ MonId }}</ar:MonId>
                <ar:FchCotiz>{{ FchCotiz }}</ar:FchCotiz>
        </ar:FEParamGetCotizacion>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposTributos = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposTributos>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposTributos>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposMonedas = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposMonedas>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposMonedas>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposIva = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposIva>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposIva>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposOpcional = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposOpcional>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposOpcional>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposConcepto = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposConcepto>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposConcepto>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetPtosVenta = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetPtosVenta>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetPtosVenta>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposCbte = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposCbte>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposCbte>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetCondicionIvaReceptor = """<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
<soap-env:Body>
    <ns0:FEParamGetCondicionIvaReceptor xmlns:ns0="http://ar.gov.afip.dif.FEV1/">
        <ns0:Auth>
            <ns0:Token>{{ Auth.Token }}</ns0:Token>
            <ns0:Sign>{{ Auth.Sign }}</ns0:Sign>
            <ns0:Cuit>{{ Auth.Cuit }}</ns0:Cuit>
        </ns0:Auth>
        {% if ClaseCmp %}
        <ns0:ClaseCmp>{{ ClaseCmp }}</ns0:ClaseCmp>
        {% endif %}
    </ns0:FEParamGetCondicionIvaReceptor>
    </soap-env:Body>
</soap-env:Envelope>
"""

FEParamGetTiposDoc = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposDoc>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposDoc>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetTiposPaises = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetTiposPaises>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposPaises>
""" + WSFEV1_TEMPLATE_EPILOGUE

FEParamGetActividades = WSFEV1_TEMPLATE_PROLOGUE + """
        <ar:FEParamGetActividades>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetActividades>
""" + WSFEV1_TEMPLATE_EPILOGUE
