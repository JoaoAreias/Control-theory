"""
	Simple program to plot the transfer functions
	of a PD, PI and PID controler.
"""
from scipy.signal import *
import matplotlib.pyplot as plt
import numpy as np


def bode_plot(sys, title):
	w, mag, phase = bode(sys)
	# Gain
	plt.subplot(2, 1, 1)
	plt.title(title)
	plt.semilogx(w, mag)
	plt.xlabel("Frequency [rad/s]")
	plt.ylabel("Gain [db]")
	# Phase
	plt.subplot(2, 1, 2)
	plt.semilogx(w, phase)
	plt.xlabel("Frequency [rad/s]")
	plt.ylabel("Phase [deg]")
	plt.show()

Kp = 1
Ki = 1
Kd = 1

PD  = TransferFunction([Kd, Kp], [1])
PI  = TransferFunction([Kp, Ki], [1, 0])
PID = TransferFunction([Kd, Kp, Ki], [1, 0])

bode_plot(PD, "PD")
bode_plot(PI, "PI")
bode_plot(PID, "PID")