# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "jrdsite"
app_title = "jrdsite"
app_publisher = "jeffrey ramirez"
app_description = "jrdsite application "
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "admin@jeffreyramirez.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jrdsite/css/jrdsite.css"
# app_include_js = "/assets/jrdsite/js/jrdsite.js"

# include js, css files in header of web template
# "/assets/jrdsite/css/main-style.css",
web_include_css = [
    "/assets/jrdsite/css/bootstrap.css",
    "/assets/jrdsite/css/style.css",
    "/assets/jrdsite/css/responsive.css",
    "/assets/jrdsite/css/animate.css",
    "/assets/jrdsite/css/colors/color1.css",
    "/assets/jrdsite/css/owl.carousel.min.css",
]
# "/assets/jrdsite/js/main-scripts.js",
web_include_js = [
    "/assets/jrdsite/js/jquery.min.js",
    "/assets/jrdsite/js/tether.min.js",
    "/assets/jrdsite/js/bootstrap.min.js",
    "/assets/jrdsite/js/jquery.easing.js",
    "/assets/jrdsite/js/parallax.js",
    "/assets/jrdsite/js/jquery-waypoints.js",
    "/assets/jrdsite/js/jquery-countTo.js",
    "/assets/jrdsite/js/jquery.countdown.js",
    "/assets/jrdsite/js/jquery.flexslider-min.js",
    "/assets/jrdsite/js/images-loaded.js",
    "/assets/jrdsite/js/jquery.isotope.min.js",
    "/assets/jrdsite/js/magnific.popup.min.js",
    "/assets/jrdsite/js/jquery.hoverdir.js",
    "/assets/jrdsite/js/owl.carousel.min.js",
    "/assets/jrdsite/js/equalize.min.js",
    "/assets/jrdsite/js/gmap3.min.js",
    "/assets/jrdsite/js/jquery-ui.js",
    "/assets/jrdsite/js/jquery.cookie.js",
    "/assets/jrdsite/js/main.js",
    "/assets/jrdsite/rev-slider/js/jquery.themepunch.tools.min.js",
    "/assets/jrdsite/rev-slider/js/jquery.themepunch.revolution.min.js",
    "/assets/jrdsite/js/rev-slider.js",
    "/assets/jrdsite/js/switcher.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.actions.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.carousel.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.kenburn.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.layeranimation.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.migration.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.navigation.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.parallax.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.slideanims.min.js",
    "/assets/jrdsite/rev-slider/js/extensions/revolution.extension.video.min.js"
]

# include js in page
# page_js = {"page" : "public/js/file.js"}
# page_js = {"main" : "public/js/main-scripts.js"}


# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "line_food"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# role_home_page = {
#     "Guest": "home"
# }


# Website user home page (by function)
# get_website_user_home_page = "jrdsite.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jrdsite.install.before_install"
# after_install = "jrdsite.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jrdsite.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jrdsite.tasks.all"
# 	],
# 	"daily": [
# 		"jrdsite.tasks.daily"
# 	],
# 	"hourly": [
# 		"jrdsite.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jrdsite.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jrdsite.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jrdsite.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jrdsite.event.get_events"
# }
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["name", "in",
                     ["Blog Post-image"]]]
    }
]
