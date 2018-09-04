import requests, subprocess, re, os, tempfile, sys, optparse, argparse

def download_file(link):
    get_response = requests.get(link)
    file_name = link.split("/")[-1]
    with open(file_name, "wb") as out_file:
	    out_file.write(get_response.content)

