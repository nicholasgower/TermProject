from genericDataProcessor import readText,loadData, pickleData
import numpy as np
import quantities as pq
from quantities.units.electromagnetism import volt,milliamp, uF,ohm
from quantities.units.temperature import degC
from quantities import Quantity as q
from quantities import UncertainQuantity as uq
import pickle
import pylatex as tex
from pylatex import TikZ,Axis,Plot,Figure,Command
from pylatex.utils import NoEscape
from pylatex.math import Math
from pylatex.table import Tabular
import matplotlib
from pylatex.position import Center
import matplotlib.pyplot as plt
