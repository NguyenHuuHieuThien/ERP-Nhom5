odoo.define('my_contacts.menu.tree', function(require) {
    "use strict";
    var KanbanController = require("web.KanbanController");
    var ListController = require("web.ListController");
    var includeDict = {
        renderButtons: function () {
            this._super.apply(this, arguments);
            var self = this;
            self.$buttons.on('click', '.my-contacts-button', function () {
                self._rpc({
                    route: '/web/action/load',
                    params: {
                        action_id: 'employment.employment_action_window',
                    },
                })
                .then(function(r) {
                    console.log(r);
                    return self.do_action(r);
                });
            });
        }
    };
    KanbanController.include(includeDict);
    ListController.include(includeDict);
});