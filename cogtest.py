from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *

import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import extra_functions

Cog = extra_functions.makeActor('phase_3.5/models/char/suitA-mod.bam', 'phase_4/models/char/suitA-neutral.bam')
CogHead = extra_functions.makeModel('phase_4/models/char/suitA-heads.bam', 'bigcheese', parent=Cog.find('**/joint_head'))

extra_functions.AnimMakeLoop(Cog, 'Anim1')

extra_functions.Smooth(Cog)


run()
