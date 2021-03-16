#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import bamboolib as bam
import os
import re
import difflib
from difflib import *
import smtplib
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import timedelta
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
import datetime
import pickle
import warnings

BASE_DIR = os.path.dirname(os.path.abspath('/Users/"YOUR PATH"'))
print(datetime.datetime.now())

def request(url):
    #Addresses server complaints on targeted pages.

    warnings.filterwarnings("ignore")
    res = requests.get(url, headers=headers, verify=False)
    warnings.filterwarnings("default")
    return res

def sendEmail(category, email, msg):
    
    #send an email about the change
    
    login =  # paste your login
    password =  # paste your password
    sender_email = #the sender email
    to =  #to fields, include additional emails here
    subject = 'CHANGE TO ' + category
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(login, password)
    wholeMsg = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail(sender_email, to, wholeMsg)
    server.quit()


#Check these links
links = {'alabama':{
            'site': 'https://www.alsde.edu/Pages/boe-events-all.aspx'},
        'alaska': {
            'site': 'https://education.alaska.gov/State_Board'},
         'arkansas': {
             'site': 'https://meetings.boardbook.org/Public/Organization/1133'},
         'california': {
             'site': 'https://www.cde.ca.gov/be/ag/ag/index.asp'},
         'colorado': {
             'site': 'https://go.boarddocs.com/co/cde/Board.nsf/Public'},
         'connecticut': {
             'site': 'https://portal.ct.gov/SDE/Board/State-Board-of-Education-Meetings/2021-Board-and-Committee-Meetings'},
         'delaware': {
             'site': 'https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S=190001'},
         'georgia': {
             'site': 'https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S=1262'},
         'hawaii': {
             'site': 'https://boe.hawaii.gov/Meetings/Notices/Pages/default.aspx'},
         'idaho': {
             'site': 'https://boardofed.idaho.gov/news-events/category/meetings/board-meeting/'},
         'illinois': {
             'site': 'https://www.isbe.net/Pages/Illinois-State-Board-of-Education-Calendar.aspx'},
         'indiana': {
             'site': 'https://www.in.gov/sboe/2427.htm'},
         'iowa': {
             'site': 'https://educateiowa.gov/iowa-state-board-education#State_Board_Meeting_Dates_Agendas_and_Minutes'},
         'kansas': {
             'site': 'https://www.ksde.org/Board/Kansas-State-Board-of-Education/Agendas-Meeting-Dates-and-Minutes/2021-Meeting-Materials-Minutes'},
         'louisiana': {
             'site': 'https://go.boarddocs.com/la/bese/Board.nsf/Public'},
         'maine': {
             'site': 'https://www.maine.gov/doe/about/leadership/stateboard/meetings/upcomingmeeting'},
         'massachusetts': {
             'site': 'https://www.doe.mass.edu/bese/boedate.html'},
         'michigan': {
             'site': 'https://www.michigan.gov/mde/0,4615,7-140-5373_16595---,00.html'},
         'mississippi': {
             'site': 'https://www.mdek12.org/MBE/Agenda2021'},
         'missouri': {
             'site': 'https://dese.mo.gov/state-board-education/agendas-minutes'},
         'montana': {
             'site': 'http://bpe.mt.gov/Home/Meeting-Schedule-and-Agendas'},
         'nebraska': {
             'site': 'https://www.education.ne.gov/stateboard/agendas/'},
         'nevada': {
             'site': 'https://doe.nv.gov/Boards_Commissions_Councils/State_Board_of_Education/Meeting_Materials/'},
         'new_jersey': {
             'site': 'https://www.nj.gov/education/sboe/meetings/agenda/2021/'},
         'new_mexico': {
             'site': 'https://webnew.ped.state.nm.us/bureaus/public-education-commission/2021-public-education-commission-meeting-information/'},
         'new_york': {
             'site': 'https://www.regents.nysed.gov/meetings'},
         'north_carolina': {
             'site': 'https://simbli.eboardsolutions.com/SB_Meetings/SB_MeetingListing.aspx?S=10399'},
         'ohio': {
             'site': 'http://education.ohio.gov/State-Board/State-Board-Meetings/State-Board-Meetings-for-2021'},
         'oklahoma': {
             'site': 'https://sde.ok.gov/state-board-education'},
         'oregon': {
             'site': 'https://meetings.boardbook.org/Public/Organization/2146'},
         'pennsylvania': {
             'site': 'https://www.stateboard.education.pa.gov/TheBoard/Meetings/Agendas/Pages/default.aspx'},
         'rhode_island': {
             'site': 'https://www.ride.ri.gov/BoardofEducation/MeetingSchedule,AgendasandMinutes.aspx'},
         'south_carolina': {
             'site': 'https://ed.sc.gov/state-board/state-board-of-education/full-board-meeting/'},
         'tennessee': {
             'site': 'https://www.tn.gov/sbe/meetings/meetings-calendar.html'},
         'texas': {
             'site': 'https://tea.texas.gov/node/358496'},
         'utah': {
             'site': 'https://usbe.civicclerk.com/web/Home.aspx'},
         'vermont': {
             'site': 'https://education.vermont.gov/calendar/list?field_event_type_tid=All&field_event_location_tid=105'},
         'virginia': {
             'site': 'https://www.doe.virginia.gov/boe/meetings/index.shtml'},
         'washington': {
             'site': 'https://www.sbe.wa.gov/2021-board-meetings'},
         'west_virginia': {
             'site': 'http://wvde.state.wv.us/minutes/current/AGENDA1.htm'},
         'wyoming': {
             'site': 'https://go.boarddocs.com/wy/wyos/Board.nsf/vpublic?open'}
}

headers = {'user-agent': 'YOUR NAME / YOUR EMAIL'}

for x in links.items():
    url = (x[1]['site'])
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    html_links = []

    for h_link in soup.find_all("a"):
        html_links.append(h_link.get("href"))

    filename = os.path.join(BASE_DIR, x[0] + '.txt')
    pageText = html_links
    pageText = str(pageText)
    pageText = pageText.replace('\t', '').replace('  ', '\n')
    cleanPage = pageText
    asciiPage = cleanPage.encode('utf-8', errors='ignore')
    splitPage = str(asciiPage).split('\n')
    alines = [w for w in splitPage if w]
    alines = str(alines)
    print(filename)
    
    with open(filename, 'rb') as o:
        blines = pickle.load(o)
        blines = str(blines)
        pickle.dump(alines, open(filename, "wb"))

    compare = difflib.SequenceMatcher(None, blines, alines).ratio()

    m = re.compile(r'(\-|\+)(\s|\w){5}')

    if compare == 1.0:
        print('There was no change on this page since last search')
        continue

    if changes != []:
        msg = 'There were some changes to this page, but they were very small. Please check the page manually.'
        print(msg)
        continue

    else:
        msg = 'There were some changes on the following page: \n' + x[1]['site'] + '\n\nBot cannot determine the extent of the changes, so I encourage you to check the website manually.'
        
        sendEmail(str(x[0]), None, msg)
        print('Sending an email, there are changes!')
