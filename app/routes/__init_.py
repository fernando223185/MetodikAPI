from flask import Flask
from app.routes.login.login import login_bp 
from app.routes.Indicadores.indicadores import verIndicadores_bp 
from app.routes.Catalogos.Usuarios import usuarios_bp, usuariosResumen_bp, actUsuario_bp, verUsuarioID_bp
from app.routes.Catalogos.Empresas import empresas_bp, empresasResumen_bp, actEmpresa_bp, verEmpresaID_bp
from app.routes.Filtros.Filtros import verFiltrosCatalogos_bp
from app.routes.Comercial.Reservas.Reservas import verReservas_bp, nvaReserva_bp


def register_routes(app: Flask):
    ##Login
    app.register_blueprint(login_bp) 
    
    ##Indicadores
    app.register_blueprint(verIndicadores_bp) 
    
    ##Catalogo Usuarios

    app.register_blueprint(usuarios_bp)  
    app.register_blueprint(usuariosResumen_bp)  
    app.register_blueprint(actUsuario_bp)
    app.register_blueprint(verUsuarioID_bp) 
    
    ##Catalogo Empresas
 
    app.register_blueprint(empresas_bp)  
    app.register_blueprint(empresasResumen_bp)  
    app.register_blueprint(actEmpresa_bp)  
    app.register_blueprint(verEmpresaID_bp)  
    
    ##Filtros
    app.register_blueprint(verFiltrosCatalogos_bp)  
    
    ##Reservas
    app.register_blueprint(verReservas_bp)  
    app.register_blueprint(nvaReserva_bp)  





  

