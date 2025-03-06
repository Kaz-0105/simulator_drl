import win32com.client
import os

vissim = win32com.client.Dispatch("Vissim.Vissim")

dir = os.getcwd()

inpx_path = dir + '\\layout\\one_lane\\network.inpx'
layx_path = dir + '\\layout\\one_lane\\network.layx'

vissim.LoadNet(inpx_path)
vissim.LoadLayout(layx_path)

print(inpx_path)

