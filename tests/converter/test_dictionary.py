#-*-:coding:utf-8-*-
import pytest
from blindtex.converter.dictionary import dictionary


Ordinary = {'alpha': [0,['alfa']], 'beta': [0,['beta']], 'gamma' : [0,['gamma']], 'delta' : [0,['delta']] ,'epsilon' : [0,['epsilon']], 'varepsilon':[0,['var epsilon']] , 'zeta' : [0,['zeta']],
            'eta':[0,['eta']], 'theta' : [0,['teta']],'vartheta':[0,['var teta']], 'iota' : [0,['iota']], 'kappa':[0,['kappa']], 'lambda':[0,['lambda']], 'mu':[0,['mi']], 'nu':[0,['ni']], 'xi':[0,['xi']],
            'pi':[0,['pi']], 'varpi': [0,['var pi']], 'rho':[0,['ro']], 'varrho': [0,['var ro']],'sigma':[0,['sigma']], 'varsigma': [0,['var sigma']], 'tau':[0,['tau']], 'upsilon':[0,['ipsilon']],
            'phi':[0,['fi']], 'varphi':[0,['var fi']], 'chi':[0,['ji']], 'psi':[0,['psi']], 'omega':[0,['omega']], 'Gamma': [0,['gama may&uacute;scula']], 'Delta':[0,['delta may&uacute;scula']],
            'Theta': [0,['teta may&uacute;scula']], 'Lambda': [0,['lambda may&uacute;scula']], 'Xi': [0,['xi may&uacute;scula']], 'Pi': [0,['pi may&uacute;scula']],
            'Sigma': [0,['sigma may&uacute;scula']], 'Upsilon': [0,['ipsilon may&uacute;scula']], 'Phi': [0,['fi may&uacute;scula']], 'Psi': [0,['psi may&uacute;scula']],
            'Omega': [0,['omega may&uacute;scula']],'aleph': [0,['alef']], 'hbar': [0,['hache barra']], 'imath': [0,['i caligr&aacute;fica, sin punto']],
            'jmath': [0,['j caligr&aacute;fica, sin punto']], 'ell' : [0,['ele caligr&aacute;fica']],'vp': [0,['p caligr&aacute;fica']], 'Re': [0,['parte real']],
            'Im': [0,['parte imaginaria']], 'partial': [0,['parcial']], 'infty': [0,['infinito']],'prime': [0,['prima']],'emptyset':[0,['conjunto vac&iacute;o']],'nabla':[0,['nabla']],
            'surd':[0,['ra&iacute;z']],'top': [0,['transpuesto']], 'bot': [0,['perpendicular']],'|': [0,['paralelo, norma']], 'angle': [0,['&aacute;ngulo']],
            'triangle': [0,['tri&aacute;ngulo']],'backslash': [0,['barra invertida']], 'forall':[0,['para todo']],'exists':[0,['existe']],'neg': [0,['negaci&oacute;n']],
            'flat': [0,['bemol']], 'natural':[0,['becuadro']],'sharp':[0,['sostenido']],'clubsuit':[0,['trebol']],'diamondsuit': [0,['diamante']],'heartsuit': [0,['corazón']],'spadsuit': [0,['picas']], 'lnot':[0,['negaci&oacute;n']]}

dOrdinary = dictionary(Ordinary)

def test_showReading():
    assert 'alfa' == dOrdinary.showReading('alpha',0)
def test_showlatex():
    assert 'alpha' == dOrdinary.showlatex('alfa')
def test_showlatexFail():
    assert 'The value %s has no LaTeX command associated.'%'alffa'  == dOrdinary.showlatex('alffa')
