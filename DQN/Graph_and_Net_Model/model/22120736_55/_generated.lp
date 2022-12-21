\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj1: 5 x0 + 20 x1 + 19 x2 + 3 x3 + 13 x4 + 20 x5 + 2 x6 + 12 x7 + 18 x8
       + 20 x9 + 17 x10 + 19 x11 + 15 x12 + 2 x13 + 19 x14 + 15 x15 + 16 x16
       + 16 x17 + 11 x18 + 18 x19 + 10 x20 + 17 x21 + 10 x22 + 17 x23 + 5 x24
       + 10 x25 + 16 x26 + 16 x27 + 3 x28 + 2 x29 + 16 x30 + 18 x31 + 14 x32
       + 10 x33 + 15 x34 + 11 x35 + 5 x36 + 9 x37 + 8 x38 + 20 x39
       + 10 maxLinkResidualBw - 10 minLinkResidualBw
Subject To
 c1:   - x0 + f0fa0 <= 0
 c2:   - x0 + f0fb0 <= 0
 c3:   - x1 + f0fa1 <= 0
 c4:   - x1 + f0fb1 <= 0
 c5:   - x2 + f0fa2 <= 0
 c6:   - x2 + f0fb2 <= 0
 c7:   - x3 + f0fa3 <= 0
 c8:   - x3 + f0fb3 <= 0
 c9:   - x4 + f0fa4 <= 0
 c10:  - x4 + f0fb4 <= 0
 c11:  - x5 + f0fa5 <= 0
 c12:  - x5 + f0fb5 <= 0
 c13:  - x6 + f0fa6 <= 0
 c14:  - x6 + f0fb6 <= 0
 c15:  - x7 + f0fa7 <= 0
 c16:  - x7 + f0fb7 <= 0
 c17:  - x8 + f0fa8 <= 0
 c18:  - x8 + f0fb8 <= 0
 c19:  - x9 + f0fa9 <= 0
 c20:  - x9 + f0fb9 <= 0
 c21:  - x10 + f0fa10 <= 0
 c22:  - x10 + f0fb10 <= 0
 c23:  - x11 + f0fa11 <= 0
 c24:  - x11 + f0fb11 <= 0
 c25:  - x12 + f0fa12 <= 0
 c26:  - x12 + f0fb12 <= 0
 c27:  - x13 + f0fa13 <= 0
 c28:  - x13 + f0fb13 <= 0
 c29:  - x14 + f0fa14 <= 0
 c30:  - x14 + f0fb14 <= 0
 c31:  - x15 + f0fa15 <= 0
 c32:  - x15 + f0fb15 <= 0
 c33:  - x16 + f0fa16 <= 0
 c34:  - x16 + f0fb16 <= 0
 c35:  - x17 + f0fa17 <= 0
 c36:  - x17 + f0fb17 <= 0
 c37:  - x18 + f0fa18 <= 0
 c38:  - x18 + f0fb18 <= 0
 c39:  - x19 + f0fa19 <= 0
 c40:  - x19 + f0fb19 <= 0
 c41:  - x20 + f0fa20 <= 0
 c42:  - x20 + f0fb20 <= 0
 c43:  - x21 + f0fa21 <= 0
 c44:  - x21 + f0fb21 <= 0
 c45:  - x22 + f0fa22 <= 0
 c46:  - x22 + f0fb22 <= 0
 c47:  - x23 + f0fa23 <= 0
 c48:  - x23 + f0fb23 <= 0
 c49:  - x24 + f0fa24 <= 0
 c50:  - x24 + f0fb24 <= 0
 c51:  - x25 + f0fa25 <= 0
 c52:  - x25 + f0fb25 <= 0
 c53:  - x26 + f0fa26 <= 0
 c54:  - x26 + f0fb26 <= 0
 c55:  - x27 + f0fa27 <= 0
 c56:  - x27 + f0fb27 <= 0
 c57:  - x28 + f0fa28 <= 0
 c58:  - x28 + f0fb28 <= 0
 c59:  - x29 + f0fa29 <= 0
 c60:  - x29 + f0fb29 <= 0
 c61:  - x30 + f0fa30 <= 0
 c62:  - x30 + f0fb30 <= 0
 c63:  - x31 + f0fa31 <= 0
 c64:  - x31 + f0fb31 <= 0
 c65:  - x32 + f0fa32 <= 0
 c66:  - x32 + f0fb32 <= 0
 c67:  - x33 + f0fa33 <= 0
 c68:  - x33 + f0fb33 <= 0
 c69:  - x34 + f0fa34 <= 0
 c70:  - x34 + f0fb34 <= 0
 c71:  - x35 + f0fa35 <= 0
 c72:  - x35 + f0fb35 <= 0
 c73:  - x36 + f0fa36 <= 0
 c74:  - x36 + f0fb36 <= 0
 c75:  - x37 + f0fa37 <= 0
 c76:  - x37 + f0fb37 <= 0
 c77:  - x38 + f0fa38 <= 0
 c78:  - x38 + f0fb38 <= 0
 c79:  - x39 + f0fa39 <= 0
 c80:  - x39 + f0fb39 <= 0
 c81:  - f0fa0 + f0fb0 - f0fa1 + f0fb1  = 0
 c82:  f0fa1 - f0fb1 - f0fa2 + f0fb2 - f0fa3 + f0fb3  = 0
 c83:  f0fa3 - f0fb3 - f0fa4 + f0fb4 - f0fa5 + f0fb5  = 0
 c84:  f0fa5 - f0fb5 - f0fa6 + f0fb6 - f0fa7 + f0fb7  = 0
 c85:  f0fa7 - f0fb7 - f0fa8 + f0fb8  = 0
 c86:  f0fa0 - f0fb0 - f0fa9 + f0fb9 - f0fa10 + f0fb10  = 0
 c87:  f0fa2 - f0fb2 + f0fa10 - f0fb10 - f0fa11 + f0fb11 - f0fa12 + f0fb12  = 0
 c88:  f0fa4 - f0fb4 + f0fa12 - f0fb12 - f0fa13 + f0fb13 - f0fa14 + f0fb14  = 0
 c89:  f0fa6 - f0fb6 + f0fa14 - f0fb14 - f0fa15 + f0fb15 - f0fa16 + f0fb16  = 0
 c90:  f0fa8 - f0fb8 + f0fa16 - f0fb16 - f0fa17 + f0fb17  = -1
 c91:  f0fa9 - f0fb9 - f0fa18 + f0fb18 - f0fa19 + f0fb19  = 0
 c92:  f0fa11 - f0fb11 + f0fa19 - f0fb19 - f0fa20 + f0fb20 - f0fa21 + f0fb21
        = 0
 c93:  f0fa13 - f0fb13 + f0fa21 - f0fb21 - f0fa22 + f0fb22 - f0fa23 + f0fb23
        = 0
 c94:  f0fa15 - f0fb15 + f0fa23 - f0fb23 - f0fa24 + f0fb24 - f0fa25 + f0fb25
        = 0
 c95:  f0fa17 - f0fb17 + f0fa25 - f0fb25 - f0fa26 + f0fb26  = 0
 c96:  f0fa18 - f0fb18 - f0fa27 + f0fb27 - f0fa28 + f0fb28  = 0
 c97:  f0fa20 - f0fb20 + f0fa28 - f0fb28 - f0fa29 + f0fb29 - f0fa30 + f0fb30
        = 0
 c98:  f0fa22 - f0fb22 + f0fa30 - f0fb30 - f0fa31 + f0fb31 - f0fa32 + f0fb32
        = 0
 c99:  f0fa24 - f0fb24 + f0fa32 - f0fb32 - f0fa33 + f0fb33 - f0fa34 + f0fb34
        = 0
 c100: f0fa26 - f0fb26 + f0fa34 - f0fb34 - f0fa35 + f0fb35  = 0
 c101: f0fa27 - f0fb27 - f0fa36 + f0fb36  = 1
 c102: f0fa29 - f0fb29 + f0fa36 - f0fb36 - f0fa37 + f0fb37  = 0
 c103: f0fa31 - f0fb31 + f0fa37 - f0fb37 - f0fa38 + f0fb38  = 0
 c104: f0fa33 - f0fb33 + f0fa38 - f0fb38 - f0fa39 + f0fb39  = 0
 c105: f0fa35 - f0fb35 + f0fa39 - f0fb39  = 0
 c106: x8 + x16 + x17 >= 1
 c107: x27 + x36 >= 1
 c108: - x0 - x1 - x2 - x3 - x4 - x5 - x6 - x7 - x8 - x9 - x10 - x11 - x12
       - x13 - x14 - x15 - x16 - x17 - x18 - x19 - x20 - x21 - x22 - x23 - x24
       - x25 - x26 - x27 - x28 - x29 - x30 - x31 - x32 - x33 - x34 - x35 - x36
       - x37 - x38 - x39 + c0 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
       + c10 + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20 + c21
       + c22 + c23 + c24  = 1
 c109: x0 - c0 <= 0
 c110: x0 - c5 <= 0
 c111: x1 - c0 <= 0
 c112: x1 - c1 <= 0
 c113: x2 - c1 <= 0
 c114: x2 - c6 <= 0
 c115: x3 - c1 <= 0
 c116: x3 - c2 <= 0
 c117: x4 - c2 <= 0
 c118: x4 - c7 <= 0
 c119: x5 - c2 <= 0
 c120: x5 - c3 <= 0
 c121: x6 - c3 <= 0
 c122: x6 - c8 <= 0
 c123: x7 - c3 <= 0
 c124: x7 - c4 <= 0
 c125: x8 - c4 <= 0
 c126: x8 - c9 <= 0
 c127: x9 - c5 <= 0
 c128: x9 - c10 <= 0
 c129: x10 - c5 <= 0
 c130: x10 - c6 <= 0
 c131: x11 - c6 <= 0
 c132: x11 - c11 <= 0
 c133: x12 - c6 <= 0
 c134: x12 - c7 <= 0
 c135: x13 - c7 <= 0
 c136: x13 - c12 <= 0
 c137: x14 - c7 <= 0
 c138: x14 - c8 <= 0
 c139: x15 - c8 <= 0
 c140: x15 - c13 <= 0
 c141: x16 - c8 <= 0
 c142: x16 - c9 <= 0
 c143: x17 - c9 <= 0
 c144: x17 - c14 <= 0
 c145: x18 - c10 <= 0
 c146: x18 - c15 <= 0
 c147: x19 - c10 <= 0
 c148: x19 - c11 <= 0
 c149: x20 - c11 <= 0
 c150: x20 - c16 <= 0
 c151: x21 - c11 <= 0
 c152: x21 - c12 <= 0
 c153: x22 - c12 <= 0
 c154: x22 - c17 <= 0
 c155: x23 - c12 <= 0
 c156: x23 - c13 <= 0
 c157: x24 - c13 <= 0
 c158: x24 - c18 <= 0
 c159: x25 - c13 <= 0
 c160: x25 - c14 <= 0
 c161: x26 - c14 <= 0
 c162: x26 - c19 <= 0
 c163: x27 - c15 <= 0
 c164: x27 - c20 <= 0
 c165: x28 - c15 <= 0
 c166: x28 - c16 <= 0
 c167: x29 - c16 <= 0
 c168: x29 - c21 <= 0
 c169: x30 - c16 <= 0
 c170: x30 - c17 <= 0
 c171: x31 - c17 <= 0
 c172: x31 - c22 <= 0
 c173: x32 - c17 <= 0
 c174: x32 - c18 <= 0
 c175: x33 - c18 <= 0
 c176: x33 - c23 <= 0
 c177: x34 - c18 <= 0
 c178: x34 - c19 <= 0
 c179: x35 - c19 <= 0
 c180: x35 - c24 <= 0
 c181: x36 - c20 <= 0
 c182: x36 - c21 <= 0
 c183: x37 - c21 <= 0
 c184: x37 - c22 <= 0
 c185: x38 - c22 <= 0
 c186: x38 - c23 <= 0
 c187: x39 - c23 <= 0
 c188: x39 - c24 <= 0
 c189: - 2 x0 + Fa0 + Fb0  = 0
 c190: - 2 x1 + Fa1 + Fb1  = 0
 c191: - 2 x2 + Fa2 + Fb2  = 0
 c192: - 2 x3 + Fa3 + Fb3  = 0
 c193: - 2 x4 + Fa4 + Fb4  = 0
 c194: - 2 x5 + Fa5 + Fb5  = 0
 c195: - 2 x6 + Fa6 + Fb6  = 0
 c196: - 2 x7 + Fa7 + Fb7  = 0
 c197: - 2 x8 + Fa8 + Fb8  = 0
 c198: - 2 x9 + Fa9 + Fb9  = 0
 c199: - 2 x10 + Fa10 + Fb10  = 0
 c200: - 2 x11 + Fa11 + Fb11  = 0
 c201: - 2 x12 + Fa12 + Fb12  = 0
 c202: - 2 x13 + Fa13 + Fb13  = 0
 c203: - 2 x14 + Fa14 + Fb14  = 0
 c204: - 2 x15 + Fa15 + Fb15  = 0
 c205: - 2 x16 + Fa16 + Fb16  = 0
 c206: - 2 x17 + Fa17 + Fb17  = 0
 c207: - 2 x18 + Fa18 + Fb18  = 0
 c208: - 2 x19 + Fa19 + Fb19  = 0
 c209: - 2 x20 + Fa20 + Fb20  = 0
 c210: - 2 x21 + Fa21 + Fb21  = 0
 c211: - 2 x22 + Fa22 + Fb22  = 0
 c212: - 2 x23 + Fa23 + Fb23  = 0
 c213: - 2 x24 + Fa24 + Fb24  = 0
 c214: - 2 x25 + Fa25 + Fb25  = 0
 c215: - 2 x26 + Fa26 + Fb26  = 0
 c216: - 2 x27 + Fa27 + Fb27  = 0
 c217: - 2 x28 + Fa28 + Fb28  = 0
 c218: - 2 x29 + Fa29 + Fb29  = 0
 c219: - 2 x30 + Fa30 + Fb30  = 0
 c220: - 2 x31 + Fa31 + Fb31  = 0
 c221: - 2 x32 + Fa32 + Fb32  = 0
 c222: - 2 x33 + Fa33 + Fb33  = 0
 c223: - 2 x34 + Fa34 + Fb34  = 0
 c224: - 2 x35 + Fa35 + Fb35  = 0
 c225: - 2 x36 + Fa36 + Fb36  = 0
 c226: - 2 x37 + Fa37 + Fb37  = 0
 c227: - 2 x38 + Fa38 + Fb38  = 0
 c228: - 2 x39 + Fa39 + Fb39  = 0
 c229: Fb0 + Fb1 <= 1.95
 c230: Fa1 + Fb2 + Fb3 <= 1.95
 c231: Fa3 + Fb4 + Fb5 <= 1.95
 c232: Fa5 + Fb6 + Fb7 <= 1.95
 c233: Fa7 + Fb8 <= 1.95
 c234: Fa0 + Fb9 + Fb10 <= 1.95
 c235: Fa2 + Fa10 + Fb11 + Fb12 <= 1.95
 c236: Fa4 + Fa12 + Fb13 + Fb14 <= 1.95
 c237: Fa6 + Fa14 + Fb15 + Fb16 <= 1.95
 c238: Fa8 + Fa16 + Fb17 <= 1.95
 c239: Fa9 + Fb18 + Fb19 <= 1.95
 c240: Fa11 + Fa19 + Fb20 + Fb21 <= 1.95
 c241: Fa13 + Fa21 + Fb22 + Fb23 <= 1.95
 c242: Fa15 + Fa23 + Fb24 + Fb25 <= 1.95
 c243: Fa17 + Fa25 + Fb26 <= 1.95
 c244: Fa18 + Fb27 + Fb28 <= 1.95
 c245: Fa20 + Fa28 + Fb29 + Fb30 <= 1.95
 c246: Fa22 + Fa30 + Fb31 + Fb32 <= 1.95
 c247: Fa24 + Fa32 + Fb33 + Fb34 <= 1.95
 c248: Fa26 + Fa34 + Fb35 <= 1.95
 c249: Fa27 + Fb36 <= 1.95
 c250: Fa29 + Fa36 + Fb37 <= 1.95
 c251: Fa31 + Fa37 + Fb38 <= 1.95
 c252: Fa33 + Fa38 + Fb39 <= 1.95
 c253: Fa35 + Fa39 <= 1.95
 c254: - x0 - maxLinkResidualBw <= -18
 c255: - x1 - maxLinkResidualBw <= -14
 c256: - x2 - maxLinkResidualBw <= -3
 c257: - x3 - maxLinkResidualBw <= -7
 c258: - x4 - maxLinkResidualBw <= -11
 c259: - x5 - maxLinkResidualBw <= -8
 c260: - x6 - maxLinkResidualBw <= -6
 c261: - x7 - maxLinkResidualBw <= -4
 c262: - x8 - maxLinkResidualBw <= -2
 c263: - x9 - maxLinkResidualBw <= -12
 c264: - x10 - maxLinkResidualBw <= -10
 c265: - x11 - maxLinkResidualBw <= -10
 c266: - x12 - maxLinkResidualBw <= -17
 c267: - x13 - maxLinkResidualBw <= -4
 c268: - x14 - maxLinkResidualBw <= -16
 c269: - x15 - maxLinkResidualBw <= -12
 c270: - x16 - maxLinkResidualBw <= -11
 c271: - x17 - maxLinkResidualBw <= -2
 c272: - x18 - maxLinkResidualBw <= -12
 c273: - x19 - maxLinkResidualBw <= -6
 c274: - x20 - maxLinkResidualBw <= -4
 c275: - x21 - maxLinkResidualBw <= -19
 c276: - x22 - maxLinkResidualBw <= -13
 c277: - x23 - maxLinkResidualBw <= -1
 c278: - x24 - maxLinkResidualBw <= -13
 c279: - x25 - maxLinkResidualBw <= -11
 c280: - x26 - maxLinkResidualBw <= -9
 c281: - x27 - maxLinkResidualBw <= -6
 c282: - x28 - maxLinkResidualBw <= -5
 c283: - x29 - maxLinkResidualBw <= -14
 c284: - x30 - maxLinkResidualBw <= -16
 c285: - x31 - maxLinkResidualBw <= -8
 c286: - x32 - maxLinkResidualBw <= -7
 c287: - x33 - maxLinkResidualBw <= -18
 c288: - x34 - maxLinkResidualBw <= -7
 c289: - x35 - maxLinkResidualBw <= -6
 c290: - x36 - maxLinkResidualBw <= -17
 c291: - x37 - maxLinkResidualBw <= -9
 c292: - x38 - maxLinkResidualBw <= -4
 c293: - x39 - maxLinkResidualBw <= -9
 c294: x0 + minLinkResidualBw <= 18
 c295: x1 + minLinkResidualBw <= 14
 c296: x2 + minLinkResidualBw <= 3
 c297: x3 + minLinkResidualBw <= 7
 c298: x4 + minLinkResidualBw <= 11
 c299: x5 + minLinkResidualBw <= 8
 c300: x6 + minLinkResidualBw <= 6
 c301: x7 + minLinkResidualBw <= 4
 c302: x8 + minLinkResidualBw <= 2
 c303: x9 + minLinkResidualBw <= 12
 c304: x10 + minLinkResidualBw <= 10
 c305: x11 + minLinkResidualBw <= 10
 c306: x12 + minLinkResidualBw <= 17
 c307: x13 + minLinkResidualBw <= 4
 c308: x14 + minLinkResidualBw <= 16
 c309: x15 + minLinkResidualBw <= 12
 c310: x16 + minLinkResidualBw <= 11
 c311: x17 + minLinkResidualBw <= 2
 c312: x18 + minLinkResidualBw <= 12
 c313: x19 + minLinkResidualBw <= 6
 c314: x20 + minLinkResidualBw <= 4
 c315: x21 + minLinkResidualBw <= 19
 c316: x22 + minLinkResidualBw <= 13
 c317: x23 + minLinkResidualBw <= 1
 c318: x24 + minLinkResidualBw <= 13
 c319: x25 + minLinkResidualBw <= 11
 c320: x26 + minLinkResidualBw <= 9
 c321: x27 + minLinkResidualBw <= 6
 c322: x28 + minLinkResidualBw <= 5
 c323: x29 + minLinkResidualBw <= 14
 c324: x30 + minLinkResidualBw <= 16
 c325: x31 + minLinkResidualBw <= 8
 c326: x32 + minLinkResidualBw <= 7
 c327: x33 + minLinkResidualBw <= 18
 c328: x34 + minLinkResidualBw <= 7
 c329: x35 + minLinkResidualBw <= 6
 c330: x36 + minLinkResidualBw <= 17
 c331: x37 + minLinkResidualBw <= 9
 c332: x38 + minLinkResidualBw <= 4
 c333: x39 + minLinkResidualBw <= 9
Bounds
 0 <= x0 <= 1
 0 <= x1 <= 1
 0 <= x2 <= 1
 0 <= x3 <= 1
 0 <= x4 <= 1
 0 <= x5 <= 1
 0 <= x6 <= 1
 0 <= x7 <= 1
 0 <= x8 <= 1
 0 <= x9 <= 1
 0 <= x10 <= 1
 0 <= x11 <= 1
 0 <= x12 <= 1
 0 <= x13 <= 1
 0 <= x14 <= 1
 0 <= x15 <= 1
 0 <= x16 <= 1
 0 <= x17 <= 1
 0 <= x18 <= 1
 0 <= x19 <= 1
 0 <= x20 <= 1
 0 <= x21 <= 1
 0 <= x22 <= 1
 0 <= x23 <= 1
 0 <= x24 <= 1
 0 <= x25 <= 1
 0 <= x26 <= 1
 0 <= x27 <= 1
 0 <= x28 <= 1
 0 <= x29 <= 1
 0 <= x30 <= 1
 0 <= x31 <= 1
 0 <= x32 <= 1
 0 <= x33 <= 1
 0 <= x34 <= 1
 0 <= x35 <= 1
 0 <= x36 <= 1
 0 <= x37 <= 1
 0 <= x38 <= 1
 0 <= x39 <= 1
      maxLinkResidualBw >= 0
      minLinkResidualBw >= 0
 0 <= f0fa0 <= 1
 0 <= f0fb0 <= 1
 0 <= f0fa1 <= 1
 0 <= f0fb1 <= 1
 0 <= f0fa2 <= 1
 0 <= f0fb2 <= 1
 0 <= f0fa3 <= 1
 0 <= f0fb3 <= 1
 0 <= f0fa4 <= 1
 0 <= f0fb4 <= 1
 0 <= f0fa5 <= 1
 0 <= f0fb5 <= 1
 0 <= f0fa6 <= 1
 0 <= f0fb6 <= 1
 0 <= f0fa7 <= 1
 0 <= f0fb7 <= 1
 0 <= f0fa8 <= 1
 0 <= f0fb8 <= 1
 0 <= f0fa9 <= 1
 0 <= f0fb9 <= 1
 0 <= f0fa10 <= 1
 0 <= f0fb10 <= 1
 0 <= f0fa11 <= 1
 0 <= f0fb11 <= 1
 0 <= f0fa12 <= 1
 0 <= f0fb12 <= 1
 0 <= f0fa13 <= 1
 0 <= f0fb13 <= 1
 0 <= f0fa14 <= 1
 0 <= f0fb14 <= 1
 0 <= f0fa15 <= 1
 0 <= f0fb15 <= 1
 0 <= f0fa16 <= 1
 0 <= f0fb16 <= 1
 0 <= f0fa17 <= 1
 0 <= f0fb17 <= 1
 0 <= f0fa18 <= 1
 0 <= f0fb18 <= 1
 0 <= f0fa19 <= 1
 0 <= f0fb19 <= 1
 0 <= f0fa20 <= 1
 0 <= f0fb20 <= 1
 0 <= f0fa21 <= 1
 0 <= f0fb21 <= 1
 0 <= f0fa22 <= 1
 0 <= f0fb22 <= 1
 0 <= f0fa23 <= 1
 0 <= f0fb23 <= 1
 0 <= f0fa24 <= 1
 0 <= f0fb24 <= 1
 0 <= f0fa25 <= 1
 0 <= f0fb25 <= 1
 0 <= f0fa26 <= 1
 0 <= f0fb26 <= 1
 0 <= f0fa27 <= 1
 0 <= f0fb27 <= 1
 0 <= f0fa28 <= 1
 0 <= f0fb28 <= 1
 0 <= f0fa29 <= 1
 0 <= f0fb29 <= 1
 0 <= f0fa30 <= 1
 0 <= f0fb30 <= 1
 0 <= f0fa31 <= 1
 0 <= f0fb31 <= 1
 0 <= f0fa32 <= 1
 0 <= f0fb32 <= 1
 0 <= f0fa33 <= 1
 0 <= f0fb33 <= 1
 0 <= f0fa34 <= 1
 0 <= f0fb34 <= 1
 0 <= f0fa35 <= 1
 0 <= f0fb35 <= 1
 0 <= f0fa36 <= 1
 0 <= f0fb36 <= 1
 0 <= f0fa37 <= 1
 0 <= f0fb37 <= 1
 0 <= f0fa38 <= 1
 0 <= f0fb38 <= 1
 0 <= f0fa39 <= 1
 0 <= f0fb39 <= 1
 0 <= c0 <= 1
 0 <= c1 <= 1
 0 <= c2 <= 1
 0 <= c3 <= 1
 0 <= c4 <= 1
 0 <= c5 <= 1
 0 <= c6 <= 1
 0 <= c7 <= 1
 0 <= c8 <= 1
 0 <= c9 <= 1
 0 <= c10 <= 1
 0 <= c11 <= 1
 0 <= c12 <= 1
 0 <= c13 <= 1
 0 <= c14 <= 1
 0 <= c15 <= 1
 0 <= c16 <= 1
 0 <= c17 <= 1
 0 <= c18 <= 1
 0 <= c19 <= 1
 0 <= c20 <= 1
 0 <= c21 <= 1
 0 <= c22 <= 1
 0 <= c23 <= 1
 0 <= c24 <= 1
Binaries
 x0  x1  x2  x3  x4  x5  x6  x7  x8  x9  x10  x11  x12  x13  x14  x15  x16 
 x17  x18  x19  x20  x21  x22  x23  x24  x25  x26  x27  x28  x29  x30  x31 
 x32  x33  x34  x35  x36  x37  x38  x39  f0fa0  f0fb0  f0fa1  f0fb1  f0fa2 
 f0fb2  f0fa3  f0fb3  f0fa4  f0fb4  f0fa5  f0fb5  f0fa6  f0fb6  f0fa7  f0fb7 
 f0fa8  f0fb8  f0fa9  f0fb9  f0fa10  f0fb10  f0fa11  f0fb11  f0fa12  f0fb12 
 f0fa13  f0fb13  f0fa14  f0fb14  f0fa15  f0fb15  f0fa16  f0fb16  f0fa17 
 f0fb17  f0fa18  f0fb18  f0fa19  f0fb19  f0fa20  f0fb20  f0fa21  f0fb21 
 f0fa22  f0fb22  f0fa23  f0fb23  f0fa24  f0fb24  f0fa25  f0fb25  f0fa26 
 f0fb26  f0fa27  f0fb27  f0fa28  f0fb28  f0fa29  f0fb29  f0fa30  f0fb30 
 f0fa31  f0fb31  f0fa32  f0fb32  f0fa33  f0fb33  f0fa34  f0fb34  f0fa35 
 f0fb35  f0fa36  f0fb36  f0fa37  f0fb37  f0fa38  f0fb38  f0fa39  f0fb39  c0 
 c1  c2  c3  c4  c5  c6  c7  c8  c9  c10  c11  c12  c13  c14  c15  c16  c17 
 c18  c19  c20  c21  c22  c23  c24 
Generals
 maxLinkResidualBw  minLinkResidualBw 
End
