import flet as ft
from pages.authentication.startup import startup
from pages.dashboard.logWindow import logWindow 
from pages.dashboard.history import history 
from pages.dashboard.resources import resources
from utils.colors import *

def views_handler(page):
    return {
        "/startup": ft.View(route="/startup", bgcolor=customBgColor, controls=[startup(page)]),
        "/logWindow": ft.View(route="/logWindow", bgcolor=customDashboardBg, controls=[logWindow(page)]),
        "/history": ft.View(route="/history", bgcolor=customDashboardBg, controls=[history(page)]),
        "/resources": ft.View(route="/resources", bgcolor=customDashboardBg, controls=[resources(page)])
    }