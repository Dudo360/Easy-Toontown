from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *

from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject

def makeActor(path, anim1=None, anim2=None, anim3=None):
    if anim1 == None:
        ActorTest = Actor(str(path))
        ActorTest.reparentTo(render)
    else:
        ActorTest = Actor(str(path), {'Anim1': str(anim1)})
        ActorTest.reparentTo(render)

    return ActorTest

def AnimMakeLoop(actor, name):
    actor.loop(str(name))

def Smooth(actor):
    actor.setBlend(frameBlend=True)

def makeModel(path, finder=None, parent=render):
    if finder != None:
        modelActor = loader.loadModel(str(path))
        foundedModel = modelActor.find('**/' + str(finder))
        foundedModel.reparentTo(parent)
        return foundedModel
    else:
        modelActor = loader.loadModel(str(path))
        modelActor.reparentTo(parent)


