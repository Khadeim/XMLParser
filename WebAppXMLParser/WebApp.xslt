<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<body>
  <h1>REST Interface</h1>
  <table border="1">
    <tr bgcolor="#E6E6FA">
      <th style="text-align:left">Operation</th>
      <th style="text-align:left">Argument(s)</th>
      <th style="text-align:left">Return</th>
      <th style="text-align:left">Exception</th>
    </tr>
    <xsl:for-each select="interface/abstract_method">
    <tr>
      <td><xsl:value-of select="@name"/></td>
      <td><xsl:for-each select="parameters">
             <xsl:for-each select="argument">
                 <xsl:if test="position() > 1">, </xsl:if>
                 <xsl:value-of select="."/>
                 <xsl:text>: </xsl:text>
                 <xsl:value-of select="@type"/>
             </xsl:for-each>
      </xsl:for-each></td>
      <td><xsl:value-of select="return"/></td>
      <xsl:choose>
          <xsl:when test="throws/exception">
           <td>Yes</td>
        </xsl:when>
        <xsl:otherwise>
           <td>No</td>
          </xsl:otherwise>
      </xsl:choose>
    </tr>
    </xsl:for-each>
  </table>
</body>

</html>

</xsl:template>

</xsl:stylesheet>

