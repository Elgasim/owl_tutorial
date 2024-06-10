from odoo import http


class Main(http.Controller):
    @http.route('/oxp/objects', type='http', auth='public')
    def list(self, **kw):
        return http.request.render(
            'oxp.listing',
            {
                'root': '/oxp',
                'objects': http.request.env['main'].search([]),
            },
        )

    @http.route('/oxp/objects/<model("main"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('oxp.object', {'object': obj})