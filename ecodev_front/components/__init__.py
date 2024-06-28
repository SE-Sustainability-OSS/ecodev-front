"""
Module containing off-the-shelf components to be used throughout the app
"""
from ecodev_front.components.card import background_card
from ecodev_front.components.card import card_section
from ecodev_front.components.card import card_title
from ecodev_front.components.card import kpi
from ecodev_front.components.card import macro_info
from ecodev_front.components.data_table import data_table
from ecodev_front.components.display_utils import get_magnitude
from ecodev_front.components.display_utils import number_formatting
from ecodev_front.components.div import centered_div
from ecodev_front.components.divider import divider
from ecodev_front.components.footer import app_footer
from ecodev_front.components.footer import footer_style
from ecodev_front.components.graph import graph_box
from ecodev_front.components.group import group
from ecodev_front.components.nav_items import navbar_action_item
from ecodev_front.components.nav_items import navbar_divider
from ecodev_front.components.nav_items import navbar_menu
from ecodev_front.components.nav_items import navbar_menu_item
from ecodev_front.components.navbar_header import app_logo
from ecodev_front.components.navbar_header import app_title
from ecodev_front.components.navbar_header import navbar_header
from ecodev_front.components.navbar_login import navbar_login
from ecodev_front.components.navlink import navlink
from ecodev_front.components.pie_chart import pie_chart
from ecodev_front.components.report_value import report_value
from ecodev_front.components.search_bar import search_bar
from ecodev_front.components.segment_control import segmented_control
from ecodev_front.components.segment_control import segmented_control_label
from ecodev_front.components.select import select
from ecodev_front.components.select import select_label
from ecodev_front.components.stack import stack
from ecodev_front.components.stepper import stepper_step
from ecodev_front.components.stepper import vertical_stepper
from ecodev_front.components.text import sub_text
from ecodev_front.components.text import text_header
from ecodev_front.components.upload_box import upload_box

__all__ = ['app_logo', 'app_title', 'navbar_header', 'navbar_menu', 'data_table', 'navbar_divider',
           'navbar_action_item', 'navbar_login', 'navbar_menu_item', 'upload_box', 'card_section',
           'card_title', 'macro_info', 'number_formatting', 'background_card', 'search_bar',
           'graph_box', 'footer_style', 'report_value', 'centered_div', 'pie_chart',
           'app_footer', 'vertical_stepper', 'stepper_step', 'group', 'segmented_control',
           'select', 'stack', 'text_header', 'sub_text', 'divider', 'kpi',
           'segmented_control_label', 'select_label', 'navlink', 'get_magnitude']
